# Brownfield Protocol (Existing Repositories)

## Discovery
- Identify current tooling and avoid breaking changes.
- Locate training entry points and evaluate how metrics are logged.
- Inventory dependency management files.

## Gap Analysis
- If linting is missing: propose adding `ruff`.
- If type checking is missing: propose adding `mypy` or keep Pyright.
- If experiment tracking is missing: propose ClearML integration.
- If the repo is flat: propose migrating to src-layout.

## Action Plan
- Present a short plan before making changes.
- Apply changes incrementally to keep the repo runnable.
- Do not remove existing tools without explicit approval.
- If tracking already exists (W&B/MLflow/ClearML), keep it and integrate with
  its dataset/versioning mechanism.
