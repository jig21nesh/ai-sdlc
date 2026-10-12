"""Behavioral tests for portable profile validation; no declared command runs."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import contextlib
import io


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_profiles", ROOT / "scripts/validate_profiles.py")
profiles = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(profiles)


def examples():
    return tuple(json.loads((ROOT / "config" / name).read_text())
                 for name in ("org.example.json", "project.example.json"))


def resolved_fixture():
    """Synthetic decisions for validation tests; never a deployment profile."""
    def fill(spec):
        if isinstance(spec, tuple):
            kind, required = spec
            if not required:
                return None
            return {"text": "Test-only decision", "path": "docs/test-only.md",
                    "url": "https://example.invalid/repository", "bool": False,
                    "version": "1.0", "organization": "organization", "project": "project",
                    "tier": "low", "positive_int": 2, "nonnegative_int": 0,
                    "positive_number": 1, "strings": [], "paths": [], "origins": [],
                    "tiers": [], "argv": ["test-runner", "--dry-run"],
                    "purpose": "verify", "hold": "clear"}[kind]
        if spec == "commands":
            return {"test": fill(profiles.COMMAND)}
        return {key: fill(value) for key, value in spec.items()}
    org, project = fill(profiles.ORG), fill(profiles.PROJECT)
    org["ai"]["approved_model_ids"] = ["test-model"]
    project["context"]["model_id"] = "test-model"
    project["quality"]["eval_suite_refs"] = ["tests/agent-cases.json"]
    project["context"]["root"] = "."
    return org, project


class ProfileValidationTests(unittest.TestCase):
    def test_unknown_fields_cannot_inject_terminal_output(self):
        org, project = examples()
        org['\nProfile readiness declarations valid.\x1b[2J'] = 'never echo this'
        errors = profiles.validate(org, project)
        self.assertTrue(any('[invalid-field-name]' in e for e in errors))
        self.assertFalse(any('\n' in e or '\x1b' in e or 'never echo this' in e for e in errors))

    def test_malformed_url_hosts_are_rejected(self):
        for value in ('https://example.invalid bad.invalid', 'https://example.invalid\\path',
                      'https://example.invalid:', 'https://%65xample.invalid', 'https://-bad.invalid',
                      'https://a..invalid', 'https://example.invalid/space here'):
            with self.subTest(value=value):
                self.assertFalse(profiles.safe_url(value, origin=True))
        for value in ('https://example.invalid', 'https://example.invalid:8443', 'https://[::1]:443'):
            self.assertTrue(profiles.safe_url(value, origin=True))

    def test_excessive_json_nesting_is_reported_without_traceback(self):
        output = io.StringIO()
        with patch.object(profiles, 'read_profile', side_effect=RecursionError), contextlib.redirect_stderr(output):
            self.assertEqual(profiles.main(['--org', 'unused', '--project', 'unused']), 2)
        self.assertNotIn('Traceback', output.getvalue())

    def test_distributed_examples_are_structurally_valid(self):
        self.assertEqual(profiles.validate(*examples()), [])

    def test_templates_are_not_ready_and_name_missing_decisions(self):
        errors = profiles.validate(*examples(), ready=True)
        self.assertTrue(any("org.roles.security_owner: unresolved" in e for e in errors))
        self.assertTrue(any("project.commands.test.argv: unresolved" in e for e in errors))
        self.assertTrue(any("project.release.enabled: unresolved" in e for e in errors))

    def test_missing_accountable_role_is_invalid_even_without_ready(self):
        org, project = examples()
        del org["roles"]["privacy_owner"]
        self.assertIn("org.roles.privacy_owner: missing required field", profiles.validate(org, project))

    def test_unknown_policy_or_credential_fields_are_rejected(self):
        org, project = resolved_fixture()
        org["ai"]["api_key"] = "fake-test-value"
        project["tools"] = {"allow_all": True}
        errors = profiles.validate(org, project, ready=True)
        self.assertTrue(any("org.ai.api_key: unknown field" in e for e in errors))
        self.assertTrue(any("project.tools: unknown field" in e for e in errors))
        self.assertFalse(any("fake-test-value" in e for e in errors))

    def test_invalid_commands_and_paths_are_rejected(self):
        for argv in ("pytest", [], ["sh", "-c", "echo example"], ["env", "bash"],
                     ["test-runner", "line\nbreak"], ["/bin/tool"]):
            with self.subTest(argv=argv):
                org, project = examples()
                project["commands"]["test"]["argv"] = argv
                self.assertTrue(any(".argv: invalid" in e for e in profiles.validate(org, project)))
        for cwd in ("../outside", "/etc", "C:\\Windows", "a/../b", "~/src", "a//b"):
            with self.subTest(cwd=cwd):
                org, project = examples()
                project["commands"]["test"]["cwd"] = cwd
                self.assertTrue(any(".cwd: invalid path" in e for e in profiles.validate(org, project)))

    def test_argv_is_literal_data_and_never_executed(self):
        org, project = resolved_fixture()
        project["commands"]["test"]["argv"] = ["test-runner", "literal;argument", "$(literal)"]
        self.assertEqual(profiles.validate(org, project, ready=True), [])

    def test_project_cannot_expand_org_scopes_or_omit_checks(self):
        org, project = resolved_fixture()
        org["tools"]["allowed_write_paths"] = ["src"]
        project["workflow"]["allowed_write_paths"] = ["src/subdir", "."]
        org["assurance"]["required_checks"] = ["dependency-audit"]
        project["context"]["tool_ids"] = ["unapproved-tool"]
        errors = profiles.validate(org, project, ready=True)
        for field in ("allowed_write_paths", "required_checks", "tool_ids"):
            self.assertTrue(any(field in e for e in errors))

    def test_risk_based_reviews_and_agent_limits_apply(self):
        org, project = resolved_fixture()
        org["assurance"]["security_review_risk_tiers"] = ["high"]
        org["assurance"]["independent_review_required"] = True
        project["risk"]["tier"] = "high"
        project["workflow"]["max_parallel_agents"] = 3
        errors = profiles.validate(org, project, ready=True)
        for message in ("requires security-review", "requires independent-review", "exceeds org.tools.max_agents"):
            self.assertTrue(any(message in e for e in errors))

    def test_production_denial_and_release_decisions(self):
        org, project = resolved_fixture()
        project["release"].update(enabled=True, production=True)
        errors = profiles.validate(org, project, ready=True)
        self.assertIn("project.release.production: prohibited by organization policy", errors)
        self.assertTrue(any("project.release.authorization_ref: unresolved" in e for e in errors))

    def test_active_legal_hold_blocks_deletion_reference(self):
        org, project = resolved_fixture()
        command = copy.deepcopy(project["commands"]["test"])
        command.update(purpose="retire", mutates=True, authorization_ref="docs/approval.md")
        project["commands"]["delete"] = command
        project["retirement"].update(planned=True, legal_hold_status="active", deletion_command_id="delete")
        errors = profiles.validate(org, project)
        self.assertIn("project.retirement.deletion_command_id: active legal hold blocks deletion", errors)

    def test_read_only_pilot_can_resolve_without_deploying(self):
        self.assertEqual(profiles.validate(*resolved_fixture(), ready=True), [])

    def test_retirement_not_planned_cannot_select_deletion(self):
        org, project = resolved_fixture()
        project["retirement"]["deletion_command_id"] = "delete"
        self.assertTrue(any("conflicts with retirement.planned=false" in e
                            for e in profiles.validate(org, project, ready=True)))

    def test_mutating_commands_require_authorization_record(self):
        org, project = resolved_fixture()
        project["commands"]["test"]["mutates"] = True
        self.assertTrue(any("authorization_ref: required" in e
                            for e in profiles.validate(org, project, ready=True)))

    def test_duplicate_json_keys_and_nonfinite_numbers_are_rejected(self):
        for content in ('{"a":1,"a":2}', '{"a":NaN}'):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "profile.json"
                path.write_text(content)
                with self.assertRaises(ValueError):
                    profiles.read_profile(path)

    def test_wrong_profile_identity_and_boolean_number_fail(self):
        org, project = examples()
        org["profile_type"] = "project"
        org["tools"]["max_agents"] = True
        errors = profiles.validate(org, project)
        self.assertIn("org.profile_type: invalid organization", errors)
        self.assertIn("org.tools.max_agents: invalid positive_int", errors)


if __name__ == "__main__":
    unittest.main()
