"""Minimal harness skeleton: explicit tool contracts, permissions, and a bounded loop.

Status: STARTER PLACEHOLDER. No model is called. The "planner" is a fixed
script so the control flow can be read, run, and tested without API keys.
Replace `scripted_planner` with a real model call when you extend this sample.

Run:
    python src/examples/minimal_harness.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


# --- Tool contracts -----------------------------------------------------------

@dataclass(frozen=True)
class Tool:
    """A tool with a declared permission scope and a required-argument list."""

    name: str
    scope: str  # "read" or "write"
    required_args: tuple[str, ...]
    run: Callable[..., Any]


def word_count(text: str) -> int:
    return len(text.split())


def save_note(text: str) -> str:
    # Placeholder side effect: a real tool would write to storage.
    return f"saved {len(text)} chars"


TOOLS: dict[str, Tool] = {
    "word_count": Tool("word_count", "read", ("text",), word_count),
    "save_note": Tool("save_note", "write", ("text",), save_note),
}


# --- Harness ------------------------------------------------------------------

@dataclass
class HarnessResult:
    status: str  # "completed" | "budget_exhausted"
    log: list[dict[str, Any]] = field(default_factory=list)


def execute(
    steps: list[dict[str, Any]],
    allowed_scopes: set[str],
    max_steps: int = 5,
) -> HarnessResult:
    """Run planned tool calls inside permission and step budgets.

    The harness, not the planner, enforces boundaries: unknown tools,
    missing arguments, and out-of-scope calls are refused and logged.
    """
    result = HarnessResult(status="completed")
    for index, step in enumerate(steps):
        if index >= max_steps:
            result.status = "budget_exhausted"
            break

        name = step.get("tool", "")
        args = step.get("args", {})
        tool = TOOLS.get(name)

        if tool is None:
            result.log.append({"tool": name, "outcome": "refused", "reason": "unknown tool"})
            continue
        if tool.scope not in allowed_scopes:
            result.log.append({"tool": name, "outcome": "refused", "reason": f"scope '{tool.scope}' not granted"})
            continue
        missing = [a for a in tool.required_args if a not in args]
        if missing:
            result.log.append({"tool": name, "outcome": "refused", "reason": f"missing args: {missing}"})
            continue

        try:
            output = tool.run(**{a: args[a] for a in tool.required_args})
            result.log.append({"tool": name, "outcome": "ok", "output": output})
        except Exception as exc:  # surface the failure, do not retry side effects
            result.log.append({"tool": name, "outcome": "error", "reason": str(exc)})
    return result


def scripted_planner(task: str) -> list[dict[str, Any]]:
    """Placeholder planner. Swap for a model call that returns the same shape."""
    return [
        {"tool": "word_count", "args": {"text": task}},
        {"tool": "save_note", "args": {"text": task}},
        {"tool": "delete_everything", "args": {}},
    ]


if __name__ == "__main__":
    task = "Summarize the harness engineering principles for the team."
    outcome = execute(scripted_planner(task), allowed_scopes={"read"})
    print(f"status: {outcome.status}")
    for entry in outcome.log:
        print(entry)
