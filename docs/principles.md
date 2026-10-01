# Engineering Principles

**Design for clarity first. Improve reliability through evidence, explicit boundaries, and focused iteration.**

## 1. Define Success Before Execution

Write acceptance criteria before implementing the workflow. Specify expected outputs, quality checks, and conditions that require human review.

## 2. Keep Modules Focused

Give each component one clear responsibility. Document its inputs, outputs, failure modes, and side effects so components can be replaced independently.

## 3. Treat Context as a Managed Resource

Supply relevant evidence with source references. Separate trusted instructions from retrieved content, preserve important decisions, and remove stale or redundant material.

## 4. Make Permissions Explicit

Grant the minimum access needed for the task. Separate read operations from writes and external actions. Enforce boundaries in the execution layer rather than relying only on model instructions.

## 5. Make State Durable and Understandable

Use an explicit state schema and record transitions. Define how interrupted work resumes and how duplicate actions are prevented.

## 6. Bound Execution and Recovery

Set limits on time, retries, tool calls, and cost. Retry transient failures with a defined policy; stop and surface repeated or permanent failures. Avoid retrying side effects unless they are idempotent or their outcome can be verified.

## 7. Validate at Meaningful Boundaries

Check tool arguments, state transitions, and final outputs. Use deterministic checks where possible and human review where judgment or consequential actions require it.

## 8. Observe Without Exposing Secrets

Record task identifiers, tool outcomes, duration, and useful failure details. Redact credentials and sensitive content. Logs should help diagnose behavior without becoming a second store of confidential data.

## 9. Evaluate Before Expanding Autonomy

Maintain representative cases for normal work, malformed inputs, tool outages, and conflicting instructions. Increase autonomy only when evidence supports it.

## 10. Grow Through Small, Verified Steps

Start with one workflow and a minimal harness. Add orchestration, memory, and integrations when they solve a demonstrated need.

## Suggested Four-Session Build Cycle

1. **Foundation:** Specify the task, contracts, and permission boundaries.
2. **Integration:** Connect tools and state with a minimal working path.
3. **Advanced:** Add justified recovery, observation, and approval features.
4. **Validation:** Exercise acceptance criteria, document limitations, and prepare a reproducible handoff.

Each session should end with a reviewable artifact and a clear checkpoint.
