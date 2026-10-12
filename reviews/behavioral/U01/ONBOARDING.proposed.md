# Try a local documentation edit

1. Open the document you want to change, read its nearby instructions, and make the bounded local edit.
2. Review the diff and run the relevant local documentation checks that actually exist in the repository. No check command was supplied in this fixture, so discover it before claiming a pass.
3. Record what changed and any checks you could not run. This local task does not require production credentials or completion of every organization/project field.

## When organization or project configuration is relevant

Use the fields needed by the current task, with real ownership for unresolved decisions. A larger organizational onboarding effort can fill the remaining fields separately. Example profiles are not accepted policy.

If you have an organization profile and a project profile, the supplied validator interface uses `--org` and `--project`:

```sh
python scripts/validate_profiles.py --org org.json --project project.json
```

The paths above are illustrative; use files that exist in your checkout. The validator also advertises `--ready`; inspect its actual help and readiness requirements before using that mode. The validator executable and profile files were not supplied with this fixture, so this command has not been run here.

Profile validation checks configuration against its implemented rules. It does not establish that runtime permissions, isolation, secrets handling, or other security controls are configured or enforced. Verify those controls separately in the actual runtime for tasks that need them.

## Retired pilot status

The deployment is reported deleted. Retirement closure is still pending: the nightly reconciliation job is reported enabled, token revocation is unverified, and retained backups require a retention/hold decision. Follow the retirement assessment before declaring closure. No schedule, credential, or data change is authorized by these instructions.
