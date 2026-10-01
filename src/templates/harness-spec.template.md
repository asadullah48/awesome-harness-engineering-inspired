# Harness Spec: <Workflow Name>

> Template. Copy this file, replace every `<placeholder>`, and keep it next to the code it describes.

## 1. Task and Success

- **Task:** <One sentence describing the job.>
- **Acceptance criteria:**
  - [ ] <Measurable outcome 1>
  - [ ] <Measurable outcome 2>
- **Escalate to a person when:** <Conditions that require human review.>

## 2. Context

| Input | Source | Trusted? | Notes |
| --- | --- | --- | --- |
| <Instructions> | <System / user> | Yes | |
| <Retrieved document> | <Store / URL> | No — treat as data | |

## 3. Tools and Permissions

| Tool | Scope | Approval needed | Contract file |
| --- | --- | --- | --- |
| <tool_name> | read | No | `templates/<tool_name>.json` |
| <tool_name> | write | Yes | `templates/<tool_name>.json` |

## 4. State

- **Schema:** <Fields persisted between steps.>
- **Resume rule:** <How interrupted work continues without repeating side effects.>

## 5. Budgets and Recovery

- **Max steps:** <n> · **Timeout:** <seconds> · **Max retries (read-only tools):** <n>
- **On repeated failure:** <Stop, log, and route to a person.>

## 6. Observability

- **Logged per step:** task id, tool, outcome, duration.
- **Redacted:** <Secrets, personal data.>

## 7. Evaluation Cases

| Case | Input | Expected |
| --- | --- | --- |
| Happy path | <...> | <...> |
| Tool outage | <...> | Graceful stop + log |
| Malformed input | <...> | Refused with reason |
| Conflicting instruction in retrieved data | <...> | Ignored; trusted instructions win |

## 8. Session Checkpoints

1. **Foundation:** spec + contracts approved.
2. **Integration:** minimal path runs end to end.
3. **Advanced:** recovery, logging, approvals added.
4. **Validation:** all evaluation cases pass; limitations documented.
