# ML Engineering Agent Manifesto

A LLM-readable protocol for bootstrapping and enforcing engineering practices in ML
projects. This repository is not a cookiecutter. It is a knowledge base that an
AI agent reads and follows to set up tooling, structure, and guardrails.

## How to use
1. Open your target project (new or existing).
2. Paste the contents of `BOOTSTRAP.md` to your agent, or point it to the raw
   file if this repo is hosted remotely.
3. Ask the agent to execute the protocol end-to-end.

Example prompts:

1) Standard execution
"Act as a Principal ML Engineer. Read and follow the protocol at
https://github.com/AlekseiSDev/ml-engineering-agent-manifesto/blob/master/BOOTSTRAP.md.
Apply it end-to-end in the current repository: analyze the codebase, select the
stack, scaffold the structure, set up tooling, and persist agent rules."

2) Silent mode (minimize questions)
"Act as a Principal ML Engineer. Read and follow the protocol at
https://github.com/AlekseiSDev/ml-engineering-agent-manifesto/blob/master/BOOTSTRAP.md.
Execute it end-to-end with minimal interruptions. Only ask questions when a
decision is blocking; otherwise pick default options and proceed."

## What the agent should do
- Decide the stack using `rules/01_stack_decision.md`
- Create the canonical project structure from `rules/02_structure.md`
- Enforce quality gates from `rules/03_quality.md`
- Add observability and experiment tracking from `rules/04_observability.md`
- For existing repositories, follow `rules/05_brownfield.md`
- Persist the rules into `.cursorrules`, `CLAUDE.md`, and
  `.github/copilot-instructions.md`

## Repository layout
- `BOOTSTRAP.md` - entry point for agents
- `rules/` - decision logic and engineering standards
- `templates/` - files to copy into the target repository

## Customization
Edit the rules and templates to match your organization requirements. Keep the
instructions short, explicit, and machine-readable.

## Versioning
Update the protocol version in `BOOTSTRAP.md` when making breaking changes.
