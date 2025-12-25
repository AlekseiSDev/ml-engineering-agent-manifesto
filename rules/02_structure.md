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
- `configs/` contains config files (YAML/TOML) for runs.
- `scripts/` contains one-off utilities and CLI entry points.
- Keep datasets out of git; use data versioning or artifact storage.
