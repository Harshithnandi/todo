import re

def validate_task_name(task_name):
    """Validate task name."""
    if not task_name.strip():
        return False, "Task name cannot be empty."
    if len(task_name) > 100:
        return False, "Task name is too long."
    return True, ""
