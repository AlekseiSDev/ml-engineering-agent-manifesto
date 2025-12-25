# Quality Gates

## Lint and Format
- Use `ruff` for linting and formatting.
- Enforce Google-style docstrings with `pydocstyle` convention.
- Keep line length consistent (default is 100 in the template).

## Type Checking
- Use `mypy` with `disallow_untyped_defs = true`.
- Add type hints to all public functions and methods.

## Pre-commit
- Use `pre-commit` with hooks for:
  - ruff
  - ruff-format
  - mypy
  - yaml/toml checks
  - end-of-file-fixer and trailing whitespace

## Makefile (optional but preferred)
- `make install` installs deps (prefer `uv`).
- `make lint` runs ruff + mypy.
- `make format` runs ruff format.
- `make test` runs pytest.

## Definition of Done
- Lint passes.
- Type checks pass.
- Tests pass (if any).
- Design doc updated when changing major behavior.
