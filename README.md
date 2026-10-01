# Awesome Harness Engineering Inspired

**Smart models are not enough. Dependable AI systems are engineered.**

This repository is a knowledge hub for **harness engineering** and **agentic AI applications**: curated resources, practical guides, and reusable frameworks that help builders turn capable models into reliable, modular, and accountable automation.

> 🧭 **Who it's for:** AI engineers, technical founders, and automation teams moving from impressive demos to dependable delivery.

---

## Why This Exists

Great automation needs more than a strong prompt. It needs:

- **Clear context** — the right evidence, nothing stale.
- **Well-defined tools** — small interfaces with explicit contracts.
- **Controlled permissions** — enforced by the system, not just requested in a prompt.
- **Durable state** — work that can be inspected and resumed.
- **Measurable feedback** — evaluations that prove the system works.

This hub brings those building blocks together in one place.

## What Is Harness Engineering?

A **harness** is the environment and control layer surrounding an AI agent: its context, tools, memory, permissions, execution lifecycle, and feedback mechanisms.

**Harness engineering** is the deliberate design of those components so an agent works within clear boundaries and produces verifiable results.

## The Framework: Harness × Loop × Graph

| Layer | Key question | Useful artifact |
| --- | --- | --- |
| **Harness** | What can the agent see and do? | Context map, tool contracts, permission policy |
| **Loop** | How does the agent detect and correct errors? | Evaluation cases, validation rules, retry budget |
| **Graph** | How does work move between steps and people? | State schema, routing rules, approval checkpoints |

Use it as a planning aid: every layer should have explicit responsibilities and observable behavior.

## Start Here

1. 📘 Read the [overview](docs/overview.md) — the core components of a harness.
2. 🧱 Apply the [principles](docs/principles.md) — ten rules for dependable systems.
3. 📚 Explore the [resources](docs/resources.md) — a curated, growing reading queue.
4. 🛠️ Run the [starter harness](src/README.md) — a minimal, dependency-free skeleton.
5. 🤝 Join in via the [contribution guide](CONTRIBUTING.md).
6. 📣 Spread the word with the [share kit](docs/share-kit.md).

## Repository Structure

```text
awesome-harness-engineering-inspired/
├── README.md                 # You are here
├── CONTRIBUTING.md           # How to contribute
├── LICENSE                   # MIT
├── .editorconfig             # Consistent formatting across editors
├── .gitignore
├── .vscode/
│   └── extensions.json       # Recommended VS Code extensions
├── docs/
│   ├── overview.md           # What a harness is and how it fits together
│   ├── principles.md         # Ten engineering principles + four-session build cycle
│   ├── resources.md          # Curated resource index and curation standard
│   └── share-kit.md          # LinkedIn / WhatsApp announcement copy
└── src/
    ├── README.md             # Guide to samples and templates
    ├── examples/
    │   └── minimal_harness.py            # Runnable starter skeleton
    └── templates/
        ├── tool-contract.template.json   # Tool contract template
        └── harness-spec.template.md      # Harness specification template
```

## Quick Start (Windows · VS Code)

```powershell
Set-Location 'D:\awesome-harness-engineering-inspired'
code .
```

Browse the guides with VS Code's Markdown preview (`Ctrl+Shift+V`). If the `code` command is unavailable, use **File → Open Folder**.

Run the starter harness (Python 3.9+, no dependencies, no API keys):

```powershell
python src/examples/minimal_harness.py
```

Optional — start version control:

```powershell
git init
git add .
git commit -m "Initial commit: harness engineering knowledge hub"
```

## Roadmap

- [x] Foundational guides and a starter resource index
- [x] Tool contract and harness spec templates
- [x] Minimal runnable harness skeleton with permission enforcement
- [ ] Real model-backed planner behind the same step contract
- [ ] State persistence, bounded retries, and structured execution logs
- [ ] Evaluation examples and human approval workflows

## Community

Bring a useful resource, a clear explanation, or a reproducible example. Small, focused contributions help the next builder move from experimentation to dependable delivery.

**Maintainer:** Asadullah Shafique · Agentic AI Developer
[GitHub](https://github.com/asadullah48) · [LinkedIn](https://www.linkedin.com/in/asadullah-shafique-a00679325/) · [Portfolio](https://asadullahshafique-devunity.vercel.app/)

## Inspiration and License

Inspired by the resource-hub approach of [Walking Labs' Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering). This project was created independently with original content; it is not a clone, fork, or affiliated project.

Original content is available under the [MIT License](LICENSE). Linked resources remain subject to their respective owners' terms and licenses.
