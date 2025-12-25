# Observability and Experiment Tracking

## ClearML (Primary)
- Initialize a ClearML `Task` at the start of every training run.
- Log hyperparameters and metrics through the ClearML logger.
- Store model artifacts in ClearML model registry when applicable.
- Use the template from `templates/tracker_clearml.py`.

## Credentials and Setup
- If `clearml.conf` is missing, ask the user to run `clearml-init`.
- If the environment has no network access, use offline or local server mode.

## Minimum Logging
- Log: dataset version, model version, git commit hash, and key metrics.
- Avoid printing metrics to stdout only; always log to the tracker.
