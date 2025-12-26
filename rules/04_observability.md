# Observability and Experiment Tracking

## ClearML (Primary)
- Initialize a ClearML `Task` at the start of every training run.
- Log hyperparameters and metrics through the ClearML logger.
- Store model artifacts in ClearML model registry when applicable.
- Use the template from `templates/tracker_clearml.py`.
- Track datasets using ClearML Data (supports S3/GS/Azure backends).

## Credentials and Setup
- If `clearml.conf` is missing, ask the user to run `clearml-init`.
- If the environment has no network access, use offline or local server mode.

## W&B (If Selected)
- Use W&B Artifacts for experiment lineage and lightweight dataset references.
- Prefer external storage (S3/GS) for large datasets.
- Do not replace ClearML Data or DVC with W&B Artifacts for primary dataset
  versioning unless the user explicitly requests it.

## Minimum Logging
- Log: dataset version, model version, git commit hash, and key metrics.
- Avoid printing metrics to stdout only; always log to the tracker.
