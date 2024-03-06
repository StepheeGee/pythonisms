import pytest
import time
from .timeup import Task, TaskManager, complete_high_priority_tasks, example_slow_function

def test_add_task():
    manager = TaskManager()
    manager.add_task("New Task", "low")
    assert len(manager) == 1

def test_add_task_priority_invalid():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("Invalid Task", "invalid_priority")

def test_complete_high_priority_tasks():
    manager = TaskManager()
    manager.add_task("High Priority Task", "high")
    complete_high_priority_tasks(manager)
    completed_tasks = [task.completed for task in manager]
    assert all(completed_tasks)

def test_complete_high_priority_tasks_no_high_priority():
    manager = TaskManager()
    manager.add_task("Low Priority Task", "low")
    complete_high_priority_tasks(manager)
    completed_tasks = [task.completed for task in manager]
    assert not any(completed_tasks)

def test_example_slow_function_time(capsys):
    with capsys.disabled():
        start_time = time.time()
        example_slow_function()
        end_time = time.time()
        assert end_time - start_time >= 1  # Check if the function took at least 1 second

def test_task_manager_equality():
    manager1 = TaskManager()
    manager1.add_task("Task 1", "high")
    manager1.add_task("Task 2", "medium")

    manager2 = TaskManager()
    manager2.add_task("Task 1", "high")
    manager2.add_task("Task 2", "medium")

    assert manager1 == manager2

def test_task_manager_truthiness():
    empty_manager = TaskManager()
    assert not empty_manager

    manager_with_tasks = TaskManager()
    manager_with_tasks.add_task("Task 1", "high")
    assert manager_with_tasks
