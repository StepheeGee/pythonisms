# Lab 42: Pythonisms

Date: 3/5/2024

## What is a pythonism?

A Pythonism typically refers to a characteristic or feature of the Python programming language that makes it unique and distinct from other programming languages. Python has its own design philosophy, often summarized as "Pythonic," which emphasizes readability, simplicity, and explicitness. Pythonisms are idiomatic expressions or practices in Python that align with this philosophy.

## Pythonic Elements

We're going to cover some of the most common Pythonic elements in Python by creating a simple task manager.

### 1. Iterators/Generators on a Custom Collection:

**Small Picture:**
- **`__iter__` Method in `TaskManager`:** This method enables the use of the `for item in custom_obj` syntax, making `TaskManager` iterable.

- **List Comprehension (`[task for task in task_manager if task.priority == 'high']`):** Provides a concise and readable way to create a list of high-priority tasks.

- **`__getitem__` Method in `TaskManager`:** Allows indexing of tasks using `task_manager[index]`.

- **Conversion to List (`list(custom_obj)`):** Demonstrates converting the custom collection to a list.

**Big Picture:**
These Pythonic features enhance code readability, expressiveness, and reduce boilerplate code. Python encourages a clean and concise syntax for working with collections.

### 2. Decorators:

**Small Picture:**
- **`timing_decorator`:** Wraps a function to calculate and print the time taken for execution.
  
- **`debug_log_decorator`:** Logs function calls and returns for debugging purposes.

- **`slow_down_decorator`:** Slows down the execution of a function by adding a delay.

**Big Picture:**
Decorators provide a powerful way to modify or extend the behavior of functions. They promote code reuse, separation of concerns, and are a key feature in Python for metaprogramming.

### 3. Dunder Methods:

**Small Picture:**
- **`__eq__` Method in `TaskManager`:** Implements equality comparison for two instances of `TaskManager`.

- **`__bool__` Method in `TaskManager`:** Defines truthiness for a `TaskManager` instance.

**Big Picture:**
Dunder methods (double underscore methods or magic methods) allow customization of how objects behave in Python. They provide a standardized way to implement common operations, making the code more readable and idiomatic.

### Pythonisms:

- **Readability and Conciseness:** Python emphasizes readability and a clean syntax. The use of list comprehensions, decorators, and dunder methods contributes to concise and expressive code.

- **Expressiveness:** Pythonic code is expressive and communicates the programmer's intent clearly. Features like decorators and dunder methods add expressive power to the code.

- **Elegance:** Pythonic code is often elegant, avoiding unnecessary complexity and providing a simple and intuitive solution to a problem.

In summary, these Pythonic elements collectively contribute to code that is readable, expressive, and follows the Python philosophy of "There should be one—and preferably only one—obvious way to do it."

## Testing

To test your code, you can use the `pytest` package.

```bash
pip install pytest
``` 

Don't forget to install the dependencies!

```bash
pip install -r requirements.txt
```