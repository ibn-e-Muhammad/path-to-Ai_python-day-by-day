# Phase 0 — Python Foundations & Data Engineering (Days 1–15)

> **Goal:** Build a solid, professional-grade Python foundation — from basic syntax all the way through Object-Oriented Programming, modular design, database integration, and a complete capstone application.

---

## 🗺️ Phase Overview

| Day(s)      | Theme                           | Key Skill                                      |
| ----------- | ------------------------------- | ---------------------------------------------- |
| Day 1       | Python Basics & Warmup          | Variables, loops, conditionals                 |
| Day 2       | Algorithms & Logic              | Searching, sorting, string manipulation        |
| Day 3       | Data Structures                 | Lists, dictionaries, slicing                   |
| Day 4       | Tuples & Comprehensions         | Multiple returns, list comprehensions          |
| Day 5       | Modules & Error Handling        | Import system, try/except                      |
| Day 6       | Recursion & Sets                | Recursion, set operations, frequency analysis  |
| Day 7       | Code Review & Refactoring       | Reading code, Pythonic patterns                |
| Day 8       | Modular Architecture            | Separation of concerns, `__main__` guard       |
| Day 9       | OOP Fundamentals                | Classes, constructors, logging                 |
| Day 10 & 11 | Advanced OOP                    | Inheritance, polymorphism, magic methods       |
| Day 12      | SQLite Databases                | CRUD operations, `DatabaseManager` class       |
| Day 13      | Base Classes & Design Patterns  | Abstract base classes, Template Method pattern |
| Day 14      | Full Data Pipeline              | End-to-end: input → process → database         |
| Day 15      | Capstone Project 1 — LifeLogger | Full CLI application with SQLite persistence   |

---

## 📅 Day-by-Day Breakdown

### Day 1 — Python Basics & Warmup

**Focus:** Getting comfortable with Python syntax and fundamental building blocks.

- **Variables & Data Types** — Working with `str` and `int`
- **f-Strings** — Dynamic string formatting with variable interpolation
- **Functions** — Defining and calling simple functions (e.g., `square`)
- **Lists** — Creating and iterating through collections of numbers
- **For Loops** — Processing list elements with `for`
- **Conditionals** — `if` statements for filtering (e.g., finding even numbers)

📁 Files: `day1_warmup.py`

---

### Day 2 — Algorithms & Logic

**Focus:** Implementing classic algorithm patterns from scratch without relying on built-ins.

- **Finding Maximum** — Manual search through a list for the largest value
- **Counting** — Iterating and counting elements that match a condition (e.g., odd numbers)
- **String Reversal** — Manually reversing a string character-by-character
- **FizzBuzz** — The classic modulo-based interview problem
- **Accumulation** — Summing numbers that meet certain criteria (e.g., evens only)
- **Filtering by Property** — Building new lists based on string characteristics (vowel starts)

📁 Files: `day2.py`

---

### Day 3 — Data Structures & Logic

**Focus:** Deeper work with Python's core data structures — lists, dictionaries, and slices.

- **List Slicing** — Advanced techniques: reversing with `[::-1]`, steps, sub-lists
- **Dictionaries** — Accessing `.keys()`, `.values()`, `.items()`
- **In-place List Transformation** — Squaring all elements of a list
- **String Processing** — Counting words that start with vowels
- **Frequency Counter** — Manually tallying word frequencies using nested loops and dicts
- **Second Largest** — Algorithm to find the 2nd largest number without sorting

📁 Files: `day3.py`

---

### Day 4 — Tuples & Data Processing

**Focus:** Working with tuples, list comprehensions, and more complex data transformations.

- **Multiple Return Values** — Returning `(min, max, sum)` as a tuple from a single function
- **String Cleaning** — Stripping whitespace and normalizing case across a list
- **Tuples** — Storing paired data (e.g., `(word, length)`) in a list of tuples
- **List Comprehensions** — Concise one-line alternatives to `for` loops
- **Dictionary Construction** — Merging two parallel lists (keys + values) into a dict
- **Combined Filter & Transform** — Squaring only odd numbers in one pass
- **Categorization** — Grouping data into `pass`/`fail` buckets using a dict of lists

📁 Files: `day4.py`

---

### Day 5 — Modules & Error Handling

**Focus:** Multi-file Python projects and defensive programming with error handling.

- **Modules & Imports** — Splitting code into `utils`, `main`, and logic files
- **Nested Lists** — Flattening lists of lists and processing sub-elements
- **List of Dictionaries** — Extracting targeted fields (e.g., names) from structured data
- **Dictionary Filtering** — Finding entries that meet threshold conditions (top scorers)
- **Error Handling** — `try-except` blocks covering `ZeroDivisionError` and `ValueError`
- **String Formatting** — Specialized output formatting for user-friendly display

📁 Files: `day5.py`, `day5_utils.py`, `day5_main.py`

---

### Day 6 — Advanced Logic & Recursion

**Focus:** Complex algorithms including recursion and deep data analysis.

- **Complex List Processing** — Averaging dictionaries, handling empty-data edge cases
- **Error Handling** — Managing `ZeroDivisionError` when computing averages
- **Frequency Analysis** — Finding the most frequently occurring word in a dataset
- **Recursion** — `deep_flatten()` to flatten arbitrarily nested lists of any depth
- **Set Operations** — Using `set()` for unique values; finding the 2nd largest unique
- **Data Cleaning** — Stripping special characters from strings with `str.strip(chars)`
- **Character Frequency** — Counting per-character occurrence in text (case-insensitive, ignoring whitespace)

📁 Files: `day6.py`

---

### Day 7 — Code Review & Refactoring

**Focus:** A dedicated review day — no new code, but critical learning through analysis.

- **Code Review** — Deep reading of Day 6 code to identify inefficiencies and code smells
- **Pythonic Thinking** — Understanding when and how to replace brute-force logic with idiomatic Python
- **Reflection** — Documenting observations and planned improvements for future days

📁 Files: `day7.py` _(minimal — reflection notes)_

---

### Day 8 — Modular Architecture & Execution Blocks

**Focus:** Structuring a multi-file Python project with clean separation of concerns.

- **Separation of Concerns** — Splitting into `data`, `utils`, and `main` modules:
  - `day8_data.py` — Raw data storage
  - `day8_utils.py` — Reusable logic and helper functions
  - `day8_mian.py` — Application entry point
- **`if __name__ == "__main__"` Guard** — Preventing unintended code execution on import
- **Local Imports** — Pulling specific variables and functions from sibling modules
- **Data Cleaning** — Stripping numbers, special characters, and whitespace from strings
- **Safe Operations** — Defensive functions that handle edge cases like empty lists (`safe_average`)

📁 Files: `day8_data.py`, `day8_utils.py`, `day8_mian.py`

---

### Day 9 — Object-Oriented Programming (OOP) & Logging

**Focus:** The pivotal transition from functional to object-oriented code, plus professional logging.

- **Classes & Objects** — Defining `DataProcessor` and `TextCleaner` blueprints and creating instances
- **Constructors (`__init__`)** — Initializing object state at creation time
- **Methods** — Encapsulating logic inside class functions
- **Logging Module** — Replacing `print()` with `logging`; configuring levels (INFO, ERROR), message formats, and file output (`app.log`)
- **Refactoring** — Converting standalone functions into class methods
- **List Comprehensions** — Writing clean, concise data-cleaning loops

📁 Files: `day9_processors.py`, `day9_cleaners.py`, `day9_main.py`

---

### Days 10 & 11 — Advanced OOP: Inheritance, Polymorphism & Magic Methods

**Focus:** Taking OOP to the next level — building class hierarchies and making objects behave like native Python types.

- **Inheritance** — `AdvancedDataProcessor` inherits from `DataProcessor`; child reuses parent logic
- **Polymorphism** — Overriding `safe_average()` in the child class with extended behavior
- **`super()`** — Calling `super().__init__()` and `super().method()` to chain parent logic cleanly
- **Magic (Dunder) Methods** — Implementing `__str__`, `__len__`, `__getitem__` so objects behave like built-in types
- **Custom Exceptions** — Defining `InvalidDataError` in `exceptions.py` for domain-specific error tracking
- **Type Checking** — Using `isinstance()` to validate input data types inside constructors
- **Extending Classes** — Adding new capabilities (`calculate_median`) to child classes

📁 Files: `day10_processors.py`, `day10_advanced_processors.py`, `day10_main.py`, `exceptions.py`

---

### Day 12 — SQLite Database Integration

**Focus:** Persistent data storage — saving program output to a real database.

- **SQLite & `sqlite3`** — Connecting to a local `.db` file; creating and querying tables
- **CRUD Operations** — Executing `INSERT`, `SELECT`, and `DELETE` SQL statements in Python
- **`DatabaseManager` Class** — Encapsulating all database logic inside a dedicated OOP class
- **Data Persistence** — Saving processed results (e.g., averages) that survive program restarts
- **Timestamps** — Using `datetime` to record exactly when each entry was saved
- **Resource Management** — Properly closing DB connections to avoid memory/file-lock issues

📁 Files: `day12_db.py`, `day12_main.py`, `day12_processors.py`

---

### Day 13 — Base Classes & Design Patterns

**Focus:** Establishing robust, scalable OOP architecture using abstract base classes.

- **Base Classes** — `BaseProcessor` defines the mandatory interface for all processor subclasses
- **Abstract Methods (via `NotImplementedError`)** — Forcing child classes to implement `_validate()` and `process()`
- **Template Method Pattern** — The parent class controls execution flow (calls `_validate` in `__init__`), children fill in the details
- **Inheritance** — `DataProcessor` and `TextCleaner` both inherit from `BaseProcessor`
- **Dictionary Returns** — `process()` returns a structured `dict` of results for flexible downstream use

📁 Files: `day13_base_processor.py`, `day13_processors.py`, `day13_cleaners.py`, `day13_main.py`

---

### Day 14 — Full Data Pipeline: Input → Process → Database

**Focus:** Connecting all previous concepts into a complete, end-to-end data processing pipeline.

- **`DatabaseHandler` Class** — Dedicated class managing SQLite connection lifecycle, table creation, and data insertion
- **End-to-End Data Flow** — Input → Validation → Processing → Persistent storage in one seamless pipeline
- **Exception Handling** — Specific `try-except` around database connections and query execution failures
- **Extensive Logging** — Every database event (success and failure) logged for production-grade debugging
- **Structured Storage** — Calculated statistics (`positives_count`, `average`, `min`, `max`) saved to `Processed_Data` table

📁 Files: `day14_database_methods.py`, `day14_processors.py`, `day14_main.py`

---

### Day 15 — Capstone Project 1: LifeLogger 🏆

**Focus:** Building a real, feature-complete console application combining everything learned in Phase 0.

**LifeLogger** is a CLI time-tracker that lets you log how many hours you spend on any topic, saves every entry permanently, and lets you review your full history.

- **Interactive CLI** — Prompts users for `Topic` and `Time Spent` in a clean input loop
- **Input Validation** — Ensures time is a numeric value and prevents negative entries
- **SQLite Persistence** — Every log entry saved to `LifeLogger_db` (topics, hours, timestamp)
- **History Reporting** — Displays all historical entries with their timestamps on demand
- **Custom Exceptions** — Domain-specific error classes in `exceptions.py` for clean error reporting
- **Application Logging** — Internal events recorded to `app.log` for debugging

📁 Files: `day15_main.py`, `day15_data_collector.py`, `day15_database_methods.py`, `exceptions.py`

---

## 🎯 Phase 0 Skills Summary

By the end of Phase 0, the following professional Python skills were acquired:

| Category             | Skills Gained                                                                       |
| -------------------- | ----------------------------------------------------------------------------------- |
| **Python Core**      | Variables, loops, conditionals, functions, list/dict/tuple, comprehensions, slicing |
| **Algorithms**       | Searching, sorting variants, frequency analysis, recursion, set operations          |
| **Error Handling**   | `try-except`, custom exception classes, input validation                            |
| **Modular Design**   | Multi-file structure, imports, `__main__` guard, separation of concerns             |
| **OOP**              | Classes, inheritance, polymorphism, magic methods, base classes, design patterns    |
| **Logging**          | `logging` module, log levels, file handlers                                         |
| **Databases**        | SQLite with `sqlite3`, CRUD, schema design, connection management                   |
| **Project Building** | Full CLI application with persistence, validation, and history reporting            |
