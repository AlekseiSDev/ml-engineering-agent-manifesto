# ML Engineering Bootstrap Protocol v1.0

## Mission
You are tasked with enforcing strict engineering standards on this repository.
You are NOT to write model or feature code yet. You are to build the factory:
structure, tooling, and governance.

## Constraints
- Ask 2-3 clarifying questions if the domain or constraints are ambiguous.
- Prefer a minimal toolset; avoid tool sprawl.
- For existing repos, do not remove or replace tools without confirmation.
- Keep changes reversible and well scoped.
- If no conflicts are found, pick sensible defaults and proceed without a
  guided install flow.

## Phase 1: Discovery
1. Inventory key files: `pyproject.toml`, `requirements.txt`, `environment.yml`,
   `setup.cfg`, `setup.py`, `Makefile`, `README.md`.
2. Identify training or evaluation entry points (e.g., `train.py`, `pipeline.py`).
3. Note whether the project is new or legacy.

## Phase 2: Stack Decision
1. Read `rules/01_stack_decision.md`.
2. Decide on:
   - Package manager
   - Linting/formatting
   - Type checking
   - Experiment tracking
   - Config management
   - Data versioning (if needed)
3. Record decisions and rationale.

## Phase 3: Structure
1. Read `rules/02_structure.md`.
2. Create the folder structure if missing.
3. Create `docs/design/` and add a design doc if none exists using
   `templates/design_doc.md`.
4. Do not write implementation code.

## Phase 4: Quality Gates
1. Read `rules/03_quality.md`.
2. Create or update:
   - `ruff.toml` from `templates/ruff.toml`
   - `.pre-commit-config.yaml` from `templates/pre-commit-config.yaml`
   - `pyproject.toml` from `templates/pyproject.toml` (if missing)
   - `Makefile` from `templates/Makefile` (optional but preferred)

## Phase 5: Observability
1. Read `rules/04_observability.md`.
2. Add ClearML integration stubs from `templates/tracker_clearml.py`.
3. If credentials are missing, ask the user to run `clearml-init` or provide
   tokens.
4. For dataset tracking, default to ClearML Data unless W&B is selected, then
   use W&B Artifacts.

## Phase 6: Governance (Persistence)
1. Write agent instructions into the appropriate files for the current agent
   (e.g., `AGENTS.md` for Codex, `.cursorrules` for Cursor, `CLAUDE.md` for
   Claude Code, `.github/copilot-instructions.md` for Copilot). Create
   `.github/` if needed.
2. Base the content on `templates/agent_rules.md`, adapting to the chosen stack.

## Phase 7: Report
- Summarize what was created or changed.
- List open questions and required user actions.
- Stop. Do not implement model or product features yet.
