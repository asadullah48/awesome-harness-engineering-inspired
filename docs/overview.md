# Harness Engineering Overview

**Build the environment that helps an agent work with clarity, accountability, and repeatable feedback.**

## The Core Idea

An AI model provides reasoning and generation capabilities. A harness connects those capabilities to a task, a set of tools, and an execution environment. Its design determines how context is supplied, actions are authorized, state is preserved, and results are checked.

## Core Components

- **Context:** Task instructions, relevant evidence, constraints, and acceptance criteria.
- **Tools:** Small interfaces with documented inputs, outputs, and error behavior.
- **State and memory:** Records of progress, decisions, and information needed to resume work.
- **Permissions:** Explicit boundaries for reading, writing, and external actions.
- **Execution control:** Timeouts, cancellation, retry limits, and recovery paths.
- **Observability:** Structured records that explain what happened and why.
- **Evaluation:** Checks that measure task completion and detect regressions.

## Modular Automation

Separate responsibilities into components with stable contracts. A retrieval component should return evidence; a planner should propose steps; an executor should perform authorized actions; a validator should check outcomes. These may be ordinary functions or services—multiple agents are useful only when the task justifies them.

## Starter Workflow

1. Define one task and its measurable acceptance criteria.
2. Supply only the context required for that task.
3. Expose the smallest useful tool set.
4. Execute within a fixed time and action budget.
5. Validate outputs before accepting completion.
6. Record results and route unresolved cases to a person.

## Example: Document Review

A review harness accepts a document and a checklist, reads the supplied material, and returns findings tied to evidence. A validator checks the output structure and required references. Any publishing action uses a separate permission boundary and approval step.

## Completion Checklist

- [ ] The task and acceptance criteria are explicit.
- [ ] Tool failures have defined recovery behavior.
- [ ] Side effects are authorized and traceable.
- [ ] State can be inspected and resumed.
- [ ] Evaluation covers success, failure, and boundary cases.

Continue with [engineering principles](principles.md) and the [resource index](resources.md).
