import time

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True
    
    def __eq__(self, other):
        return (
            isinstance(other, Task) and
            self.title == other.title and
            self.priority == other.priority and
            self.completed == other.completed
        )

class TaskManager:
    def __init__(self):
        self.tasks = []

    
    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)

    def __iter__(self):
        return iter(self.tasks)

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, index):
        return self.tasks[index]

    def __eq__(self, other):
        # Compare TaskManagers based on their tasks
        return self.tasks == other.tasks

    def __bool__(self):
        # Consider TaskManager truthy if it has tasks
        return bool(self.tasks)

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

def debug_log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def slow_down_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)  # Simulate a slow function
        return func(*args, **kwargs)
    return wrapper

@timing_decorator
@debug_log_decorator
def complete_high_priority_tasks(task_manager):
    high_priority_tasks = [task for task in task_manager if task.priority == 'high']
    for task in high_priority_tasks:
        task.complete()

@slow_down_decorator
def example_slow_function():
    print("This is a slow function")

def main():
    # Create a task manager
    manager = TaskManager()

    # Add tasks
    manager.add_task("Write Pythonic Project", "high")
    manager.add_task("Learn Python Decorators", "medium")
    manager.add_task("Implement Task Manager", "high")

    # Display tasks before completion
    print("Tasks before completion:")
    for task in manager:
        print(f"{task.title} - Priority: {task.priority} - Completed: {task.completed}")

    # Complete high-priority tasks
    complete_high_priority_tasks(manager)

    # Display tasks after completion
    print("\nTasks after completion:")
    for task in manager:
        print(f"{task.title} - Priority: {task.priority} - Completed: {task.completed}")

    # Demonstrate decorators
    example_slow_function()

    # Demonstrate dunder methods
    empty_manager = TaskManager()
    if manager == empty_manager:
        print("Task managers are equal.")
    
    if manager:
        print("Task manager is truthy.")
    else:
        print("Task manager is falsy.")

if __name__ == "__main__":
    main()
