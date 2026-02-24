# Day 10 & 11: Advanced OOP and Error Handling

## Overview

This folder contains the code for Days 10 and 11, focusing on advanced Object-Oriented Programming (OOP) concepts to build robust and scalable applications.

## Key Concepts Covered

- **Inheritance**: Creating a child class (`AdvancedDataProcessor`) that inherits properties and methods from a parent class (`DataProcessor`).
- **Polymorphism**: Overriding methods (like `safe_average`) in the child class to provide specialized behavior.
- **Super()**: Using `super().__init__` and `super().method()` to reuse parent class logic.
- **Magic Methods**: Implementing `__str__`, `__len__`, and `__getitem__` to make objects behave like built-in Python types.
- **Custom Exceptions**: Defining and raising specific errors (e.g., `InvalidDataError`) for better error tracking.
- **Type Checking**: Using `isinstance()` to validate input data types in constructors.
- **Extending Functionality**: Adding new methods (like `calculate_median`) to child classes.

## Code Files

- `day10_processors.py`: Base class `DataProcessor` with initialization and basic stats.
- `day10_advanced_processors.py`: Child class `AdvancedDataProcessor` extending the base class.
- `day10_main.py`: Main script to test inheritance and error handling.
- `exceptions.py`: Custom exception definitions.
