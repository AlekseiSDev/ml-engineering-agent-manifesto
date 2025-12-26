# Canonical Project Structure

Use a src-layout and keep docs and configs explicit. Create only what is needed
for the current project.

```
<project>/
  docs/
    design/
  src/
    <package_name>/
      __init__.py
      config.py
      data/
      models/
      training/
      evaluation/
      tests/
        test_<module>.py
  configs/
  scripts/
  data/
    raw/
    interim/
    processed/
  notebooks/  (optional)
```

Guidelines:
- `docs/design/` holds design docs before feature implementation.
- `src/<package_name>/config.py` uses Pydantic Settings (see `templates/config.py`).
- Tests are colocated with code under `src/<package_name>/tests/` or alongside
  modules as `test_*.py` when appropriate.
- `configs/` contains config files (YAML/TOML) for runs.
- `scripts/` contains one-off utilities and CLI entry points.
- Keep datasets out of git; use ClearML Data by default, or DVC if git-like
  versioning/pipelines are needed. W&B Artifacts can be used for lightweight
  lineage when W&B is selected.
