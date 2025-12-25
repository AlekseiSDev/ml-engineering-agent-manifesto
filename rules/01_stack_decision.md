# Stack Decision Tree

## Principles
- Prefer a minimal, consistent toolset.
- Default to fast and strict tools.
- Do not replace existing tools without user confirmation.

## Dependency Management
- If `pyproject.toml` + `poetry.lock` exist: keep Poetry.
- If `environment.yml` exists: keep Conda unless user prefers `uv`.
- If `requirements.txt` exists and no lock file: suggest migrating to `uv`.
- For new projects: use `uv` by default.

## Linting and Formatting
- Primary: `ruff` (single tool for lint + format).
- If an existing formatter is present (Black/Isort/Flake8): keep it unless the
  user wants consolidation.

## Type Checking
- Primary: `mypy`.
- If the repo already uses Pyright: keep Pyright.

## Experiment Tracking
- Primary: **ClearML**.
  - If `clearml.conf` is missing, ask the user to run `clearml-init` or to use
    offline/local server mode.
- If ClearML is forbidden: use W&B.

## Config Management
- Default: Pydantic Settings for lightweight configs.
- For large or multi-environment projects: consider Hydra.

## Data Versioning
- If datasets > 1GB or multi-stage pipelines: suggest DVC.
- Otherwise: use ClearML Data or track dataset artifacts in storage.
