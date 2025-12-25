from __future__ import annotations

from clearml import Task


def init_task(
    project_name: str,
    task_name: str,
    tags: list[str] | None = None,
) -> Task:
    """Initialize a ClearML Task for experiment tracking."""
    return Task.init(project_name=project_name, task_name=task_name, tags=tags or [])


def get_logger(task: Task):
    """Get a ClearML logger for metric reporting."""
    return task.get_logger()
