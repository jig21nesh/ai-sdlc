#!/usr/bin/env python3
"""Validate inert AI-SDLC profile declarations; never execute their commands."""
import argparse
import ipaddress
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit


# A tuple is (value kind, required for readiness). Every named field is required
# structurally; unresolved leaf values are null in the distributed templates.
def field(kind, ready=True):
    return (kind, ready)


ROLES = ("engineering_owner", "product_owner", "security_owner", "privacy_owner",
         "quality_owner", "release_owner", "service_owner", "incident_commander",
         "retention_owner")
TIERS = {"low", "moderate", "high", "critical"}
PURPOSES = {"verify", "build", "deploy", "rollback", "operate", "retire"}
COMMAND = {
    "argv": field("argv"), "cwd": field("path"),
    "purpose": field("purpose"), "timeout_seconds": field("positive_int"),
    "mutates": field("bool"), "authorization_ref": field("path", False),
}
ORG = {
    "schema_version": field("version"), "profile_type": field("organization"),
    "profile_id": field("text"), "policy_version": field("text"),
    "roles": {role: field("text") for role in ROLES},
    "data": {
        "classifications": field("strings"), "allowed_context_classes": field("strings"),
        "approved_source_locations": field("strings"), "residency_regions": field("strings"),
        "retention_days": field("nonnegative_int"), "provider_retention_days": field("nonnegative_int"),
        "training_use_allowed": field("bool"), "legal_hold_process_ref": field("path"),
        "deletion_verification_process_ref": field("path"),
    },
    "ai": {
        "approved_model_ids": field("strings"), "provider_terms_review_ref": field("path"),
        "evaluation_policy_ref": field("path"), "model_change_review_required": field("bool"),
    },
    "tools": {
        "allowed_tool_ids": field("strings"), "allowed_read_paths": field("paths"),
        "allowed_write_paths": field("paths"), "allowed_network_origins": field("origins"),
        "max_agents": field("positive_int"), "max_task_seconds": field("positive_int"),
        "max_task_cost_usd": field("positive_number"),
        "authorization_policy_ref": field("path"), "runtime_controls_ref": field("path"),
    },
    "assurance": {
        "required_checks": field("strings"), "independent_review_required": field("bool"),
        "security_review_risk_tiers": field("tiers"), "usability_review_required": field("bool"),
        "exception_process_ref": field("path"), "evidence_retention_days": field("nonnegative_int"),
    },
    "release": {
        "approval_required": field("bool"), "authorized_environment_ids": field("strings"),
        "production_deployment_allowed": field("bool"), "rollback_evidence_required": field("bool"),
        "approval_policy_ref": field("path"),
    },
    "operations": {
        "incident_process_ref": field("path"), "severity_thresholds_ref": field("path"),
        "notification_policy_ref": field("path"), "access_review_days": field("positive_int"),
        "emergency_stop_process_ref": field("path"),
    },
}
PROJECT = {
    "schema_version": field("version"), "profile_type": field("project"),
    "context": {
        "id": field("text"), "description": field("text"), "repository_url": field("url"),
        "root": field("path"), "instructions_paths": field("paths"),
        "artifact_dir": field("path"), "adapter_profile_ref": field("path"),
        "model_id": field("text"), "ai_data_classes": field("strings"),
        "tool_ids": field("strings"), "network_origins": field("origins"),
    },
    "product": {
        "problem_statement": field("text"), "users": field("strings"),
        "success_metrics": field("strings"), "requirements_ref": field("path"),
        "accessibility_target": field("text"),
    },
    "risk": {
        "tier": field("tier"), "rationale": field("text"), "data_classes": field("strings"),
        "contains_ai_product_features": field("bool"), "threats_ref": field("path"),
        "approved_exception_refs": field("paths"),
    },
    "quality": {
        "required_checks": field("strings"), "acceptance_ref": field("path"),
        "eval_suite_refs": field("paths"), "performance_budgets_ref": field("path"),
        "security_verification_ref": field("path"), "accessibility_verification_ref": field("path"),
    },
    "architecture": {
        "overview_ref": field("path"), "decision_record_dir": field("path"),
        "interfaces_ref": field("path"), "dependency_manifest_paths": field("paths"),
        "data_flow_ref": field("path"), "migration_plan_ref": field("path"),
    },
    "workflow": {
        "branch_strategy": field("text"), "review_policy_ref": field("path"),
        "task_artifact_dir": field("path"), "max_parallel_agents": field("positive_int"),
        "allowed_read_paths": field("paths"), "allowed_write_paths": field("paths"),
        "stop_conditions": field("strings"),
    },
    "commands": "commands",
    "release": {
        "enabled": field("bool"), "target_environment_id": field("text", False),
        "production": field("bool", False), "artifact_dir": field("path"),
        "provenance_ref": field("path", False), "deploy_command_id": field("text", False),
        "rollback_command_id": field("text", False), "rollout_plan_ref": field("path", False),
        "restore_plan_ref": field("path", False), "authorization_ref": field("path", False),
    },
    "operations": {
        "slo_ref": field("path"), "telemetry_ref": field("path"),
        "runbooks_dir": field("path"), "on_call_ref": field("path"),
        "incident_record_dir": field("path"), "kill_switch_ref": field("path"),
    },
    "retirement": {
        "planned": field("bool"), "dependency_inventory_ref": field("path", False),
        "transition_plan_ref": field("path", False), "retention_plan_ref": field("path", False),
        "legal_hold_status": field("hold", False), "disposition_approval_ref": field("path", False),
        "deletion_command_id": field("text", False), "closure_evidence_dir": field("path"),
    },
}


def clean_text(value):
    return (isinstance(value, str) and bool(value.strip()) and len(value) <= 4096
            and not any(ord(c) < 32 or ord(c) == 127 for c in value))


def safe_path(value):
    """Lexical portability check only; runtime must resolve symlinks and roots."""
    return (clean_text(value) and not value.startswith(("/", "~"))
            and not any(c in value for c in "\\:*?\"<>|#")
            and ".." not in value.split("/") and "//" not in value
            and str(PurePosixPath(value)) == value)


def safe_url(value, origin=False):
    if not clean_text(value) or any(c.isspace() for c in value) or '\\' in value:
        return False
    try:
        parsed = urlsplit(value)
        port = parsed.port
    except ValueError:
        return False
    host = parsed.hostname
    if not host or '%' in host or parsed.netloc.endswith(':'):
        return False
    try:
        ipaddress.ip_address(host)
    except ValueError:
        try:
            ascii_host = host.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        if len(ascii_host) > 253 or any(not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?', label)
                                        for label in ascii_host.split('.')):
            return False
    return (parsed.scheme == "https" and bool(host)
            and parsed.username is None and parsed.password is None
            and not parsed.query and not parsed.fragment
            and (not origin or parsed.path in ("", "/"))
            and (port is None or 1 <= port <= 65535))


def kind_valid(value, kind):
    if kind in {"text", "path", "url"}:
        return {"text": clean_text, "path": safe_path, "url": safe_url}[kind](value)
    if kind == "bool":
        return type(value) is bool
    if kind in {"positive_int", "nonnegative_int"}:
        return type(value) is int and value >= (1 if kind == "positive_int" else 0)
    if kind == "positive_number":
        return type(value) in (int, float) and 0 < value < float("inf")
    if kind in {"version", "organization", "project", "tier", "purpose", "hold"}:
        choices = {"version": {"1.0"}, "organization": {"organization"},
                   "project": {"project"}, "tier": TIERS, "purpose": PURPOSES,
                   "hold": {"clear", "active"}}
        return isinstance(value, str) and value in choices[kind]
    if kind in {"strings", "paths", "origins", "tiers"}:
        check = {"strings": clean_text, "paths": safe_path,
                 "origins": lambda x: safe_url(x, True),
                 "tiers": lambda x: isinstance(x, str) and x in TIERS}[kind]
        return (isinstance(value, list) and all(check(x) for x in value)
                and len(set(value)) == len(value))
    if kind == "argv":
        if not isinstance(value, list) or not value or not all(clean_text(x) for x in value):
            return False
        executable = value[0]
        if not safe_path(executable):
            # A conventional ./tool spelling is accepted for an executable only.
            if not executable.startswith("./") or not safe_path(executable[2:]):
                return False
        shells = {"sh", "bash", "zsh", "fish", "csh", "ksh", "cmd", "cmd.exe",
                  "powershell", "powershell.exe", "pwsh", "env", "sudo"}
        return PurePosixPath(executable).name.lower() not in shells
    raise AssertionError("Unknown internal kind")


def check_shape(value, spec, location, ready, errors):
    if isinstance(spec, tuple):
        kind, required = spec
        if value is None:
            if ready and required:
                errors.append(f"{location}: unresolved decision (null); set {kind}")
        elif not kind_valid(value, kind):
            errors.append(f"{location}: invalid {kind}")
        return
    if not isinstance(value, dict):
        errors.append(f"{location}: expected object")
        return
    if spec == "commands":
        for name, command in value.items():
            if not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", name):
                errors.append(f"{location}: invalid command identifier")
                continue
            check_shape(command, COMMAND, f"{location}.{name}", ready, errors)
        return
    for name in sorted(set(value) - set(spec)):
        label = name if re.fullmatch(r'[A-Za-z0-9_-]{1,64}', name) else '[invalid-field-name]'
        errors.append(f"{location}.{label}: unknown field; policy overrides and credential values are not accepted")
    for name, child in spec.items():
        if name not in value:
            errors.append(f"{location}.{name}: missing required field")
        else:
            check_shape(value[name], child, f"{location}.{name}", ready, errors)


def covered(path, allowed):
    return any(prefix == "." or path == prefix or path.startswith(prefix + "/") for prefix in allowed)


def validate(org, project, ready=False):
    errors = []
    check_shape(org, ORG, "org", ready, errors)
    check_shape(project, PROJECT, "project", ready, errors)
    # Shape errors must not cause a traceback, and comparisons require valid types.
    shape_errors = []
    check_shape(org, ORG, "org", False, shape_errors)
    check_shape(project, PROJECT, "project", False, shape_errors)
    if shape_errors:
        return errors

    def subset(chosen, allowed, label):
        if chosen is not None and allowed is not None and not set(chosen) <= set(allowed):
            errors.append(f"{label}: selection exceeds organization policy")

    subset(project["context"]["ai_data_classes"], org["data"]["allowed_context_classes"], "project.context.ai_data_classes")
    subset(project["risk"]["data_classes"], org["data"]["classifications"], "project.risk.data_classes")
    subset(org["data"]["allowed_context_classes"], org["data"]["classifications"], "org.data.allowed_context_classes")
    subset(project["context"]["tool_ids"], org["tools"]["allowed_tool_ids"], "project.context.tool_ids")
    subset(project["context"]["network_origins"], org["tools"]["allowed_network_origins"], "project.context.network_origins")
    if project["context"]["model_id"] is not None:
        subset([project["context"]["model_id"]], org["ai"]["approved_model_ids"], "project.context.model_id")
    for key in ("allowed_read_paths", "allowed_write_paths"):
        chosen, allowed = project["workflow"][key], org["tools"][key]
        if chosen is not None and allowed is not None and any(not covered(p, allowed) for p in chosen):
            errors.append(f"project.workflow.{key}: paths exceed organization policy")
    chosen, allowed = project["workflow"]["max_parallel_agents"], org["tools"]["max_agents"]
    if chosen is not None and allowed is not None and chosen > allowed:
        errors.append("project.workflow.max_parallel_agents: exceeds org.tools.max_agents")
    checks = project["quality"]["required_checks"]
    subset(org["assurance"]["required_checks"], checks, "project.quality.required_checks (missing organization checks)")
    if checks is not None:
        required = []
        if org["assurance"]["independent_review_required"] is True:
            required.append("independent-review")
        if org["assurance"]["usability_review_required"] is True:
            required.append("usability-review")
        if project["risk"]["tier"] in (org["assurance"]["security_review_risk_tiers"] or []):
            required.append("security-review")
        for item in required:
            if item not in checks:
                errors.append(f"project.quality.required_checks: organization policy requires {item}")
    for name, command in project["commands"].items():
        limit = org["tools"]["max_task_seconds"]
        if limit is not None and command["timeout_seconds"] is not None and command["timeout_seconds"] > limit:
            errors.append(f"project.commands.{name}.timeout_seconds: exceeds organization task limit")
        if command["purpose"] in {"deploy", "rollback", "operate", "retire"} and command["mutates"] is False:
            errors.append(f"project.commands.{name}.mutates: consequential command must declare mutation")
        if ready and command["mutates"] is True and command["authorization_ref"] is None:
            errors.append(f"project.commands.{name}.authorization_ref: required for mutating command; reference is not proof of authorization")
    release = project["release"]
    if release["production"] is True and org["release"]["production_deployment_allowed"] is False:
        errors.append("project.release.production: prohibited by organization policy")
    if release["target_environment_id"] is not None:
        subset([release["target_environment_id"]], org["release"]["authorized_environment_ids"], "project.release.target_environment_id")

    def need(container, keys, prefix):
        for key in keys:
            if container[key] is None:
                errors.append(f"{prefix}.{key}: unresolved decision required for enabled activity")

    def command_ref(container, key, purpose, prefix):
        name = container[key]
        if name is not None and (name not in project["commands"] or project["commands"][name]["purpose"] != purpose):
            errors.append(f"{prefix}.{key}: must name a declared {purpose} command")

    command_ref(release, "deploy_command_id", "deploy", "project.release")
    command_ref(release, "rollback_command_id", "rollback", "project.release")
    retirement = project["retirement"]
    command_ref(retirement, "deletion_command_id", "retire", "project.retirement")
    if retirement["legal_hold_status"] == "active" and retirement["deletion_command_id"] is not None:
        errors.append("project.retirement.deletion_command_id: active legal hold blocks deletion")
    if retirement["deletion_command_id"] is not None and retirement["planned"] is False:
        errors.append("project.retirement.deletion_command_id: deletion conflicts with retirement.planned=false")
    if ready:
        if not project["commands"] or not any(c["purpose"] == "verify" for c in project["commands"].values()):
            errors.append("project.commands: declare at least one verify command")
        if not project["quality"]["eval_suite_refs"]:
            errors.append("project.quality.eval_suite_refs: provide a representative agent/skill evaluation suite")
        if release["enabled"] is True:
            need(release, ["target_environment_id", "production", "provenance_ref", "deploy_command_id",
                           "rollout_plan_ref", "restore_plan_ref", "authorization_ref"], "project.release")
            if org["release"]["rollback_evidence_required"] is True:
                need(release, ["rollback_command_id"], "project.release")
        if retirement["planned"] is True:
            need(retirement, ["dependency_inventory_ref", "transition_plan_ref", "retention_plan_ref",
                              "legal_hold_status", "disposition_approval_ref"], "project.retirement")
    return errors


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON field")
        result[key] = value
    return result


def read_profile(filename):
    with Path(filename).open("rb") as stream:
        raw = stream.read(1_048_577)
    if len(raw) > 1_048_576:
        raise ValueError("profile exceeds 1 MiB")
    return json.loads(raw, object_pairs_hook=unique_object,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError("non-finite JSON number")))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--org", required=True, help="organization JSON profile")
    parser.add_argument("--project", required=True, help="project JSON profile")
    parser.add_argument("--ready", action="store_true", help="also reject unresolved readiness decisions")
    args = parser.parse_args(argv)
    try:
        org, project = read_profile(args.org), read_profile(args.project)
    except (OSError, ValueError, UnicodeError, RecursionError) as exc:
        # Do not echo file content or potentially sensitive parser context.
        print(f"Profile input error: {type(exc).__name__}; use readable, unique-field UTF-8 JSON under 1 MiB.", file=sys.stderr)
        return 2
    errors = validate(org, project, args.ready)
    if errors:
        print("Profile validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Profile readiness declarations valid." if args.ready else "Profile structure valid; null decisions may remain.")
    print("No commands executed. References, runtime permissions, approvals, and certification were not verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
