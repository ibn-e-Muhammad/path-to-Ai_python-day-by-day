# Day 13: Base Classes and Inheritance Patterns

## Overview

This folder contains the code for Day 13, focusing on building a strong object-oriented foundation using Base Classes and enforcing interface consistency.

## Key Concepts Covered

- **Base Classes**: Creating a generic `BaseProcessor` class to define the expected structure for all processor types.
- **Abstract Methods**: Using `NotImplementedError` to force child classes to provide their own implementations for critical methods like `_validate` and `process`.
- **Template Method Pattern**: Defining the flow of execution in the parent class (e.g., calling `_validate` inside `__init__`) to ensure consistent initialization logic across all subclasses.
- **Inheritance**: `DataProcessor` inherits from `BaseProcessor`, gaining its structure while providing specific logic for number processing.
- **Dictionary Returns**: Returning a dictionary of results from the `process` method for flexible data consumption.

## Code Files

- `day13_base_processor.py`: The parent class defining the contract.
- `day13_processors.py`: The concrete implementation for numeric data.
- `day13_cleaners.py`: The concrete implementation for text data.
- `day13_main.py`: The execution script.
