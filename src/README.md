# Code Samples

**Turn documented principles into small, reproducible examples.**

This folder holds starter placeholders. They are intentionally minimal: readable, dependency-free, and safe to run.

## What's Here

| Path | Type | Status |
| --- | --- | --- |
| `examples/minimal_harness.py` | Runnable skeleton (Python 3.9+, standard library only) | Starter — scripted planner, no model call |
| `templates/tool-contract.template.json` | Tool contract template | Fill-in template |
| `templates/harness-spec.template.md` | Harness specification template | Fill-in template |
| `examples/.gitkeep`, `templates/.gitkeep` | Folder placeholders | Keep |

## Run the Skeleton

From the project root in PowerShell:

```powershell
python src/examples/minimal_harness.py
```

Expected output: the read-only tool runs, the write tool is refused because only the `read` scope is granted, and the unknown tool is refused. This demonstrates that boundaries are enforced by the harness, not by the planner.

## Proposed Next Samples

1. Replace the scripted planner with a real model call that returns the same step format.
2. Add persisted state, bounded retries for read-only tools, and cancellation.
3. Add an evaluation runner covering success, tool failure, and invalid output.

## Sample Quality Standard

- Explain the problem, prerequisites, and how to run the sample.
- Document expected output and known limitations.
- Keep secrets out of source files and provide placeholder configuration.
- Declare dependencies and their licenses.
- Include meaningful checks for behavior and failure paths.
- Keep external writes opt-in and clearly documented.
