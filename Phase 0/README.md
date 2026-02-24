# 🧗 The Iron-Clad Data Science Ladder

> _"If it isn't in a repo, it doesn't exist."_

This repository documents a structured, no-shortcuts journey from **Python Engineer → Data Scientist → ML Engineer → Deep Learning → NLP → Computer Vision → Robotics**. The full plan is divided into 6 coding phases, each building directly on the last, and each ending with a real capstone project.

---

## 📋 The Daily Operating System (3–5 Hours/Day)

Every study day follows the same structure to fight the memory leak problem:

| Hour                             | Activity                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Hour 1** — The Intake          | Theory only. Watch videos / read docs. Hard stop at 1 hour.                                     |
| **Hours 2–3** — The Lab          | Write the code from scratch, without looking at the tutorial. If you peek, you reset the timer. |
| **Hour 4** — The Integration     | Add what you learned today to yesterday's project. Keep building.                               |
| **Hour 5** — Review _(optional)_ | Debugging and git commits. No code stays on your PC overnight.                                  |

---

## 🗺️ Full Learning Roadmap

### 🏗️ Phase 0 — The Python Engineer _(Weeks 1–4)_

**Goal:** Stop writing "Scripting Python" and start writing "Software Python." Data science pipelines are complex software systems.

| Topic                           | The Real Task                                                                                   | Retention Check                                                |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **1. Git**                      | Create a repo. Learn `init`, `add`, `commit`, `push`.                                           | Rule: No code stays on your PC overnight. Push everything.     |
| **2. Modular Python & Logging** | Create a `logger.py` module. Import it into a main script.                                      | Stop using `print()`. Use `logging.info()`.                    |
| **3. OOP & Exceptions**         | Create a `DataHandler` class. It must ingest a CSV and crash gracefully if the file is missing. | If your code crashes with a raw traceback, you fail. Catch it. |
| **4. SQLite & Persistence**     | Save your processed data to `data.db` via your class methods.                                   | Write a query to fetch the last 5 entries.                     |

🔥 **Capstone 1 — The "Life Logger" CLI**

> A terminal app to track your 3–5 hours of study.
>
> - **Input:** `python run.py --add "Studied Pandas" --hours 3`
> - **Logic:** A `StudySession` class validates input (no negative hours)
> - **Storage:** Saves to SQLite
> - **Output:** `logging` writes "Session saved" to `app.log`
> - **Git:** Push it.

📁 **Folder:** `Phase 0/` ← _You are here_

---

### 📊 Phase 1 — The Data Mechanic _(Weeks 5–9)_

**Goal:** You cannot model what you cannot clean.
**Focus:** Pandas, NumPy, Visualization, Statistics.

| Topic                      | The Real Task                                                                | Retention Check                                     |
| -------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------- |
| **5. NumPy & Vectors**     | Manually implement Mean Squared Error using numpy arrays — no loops allowed. | Speed test: Loop vs Vectorization.                  |
| **6. Pandas Core**         | Load a messy dataset. Fix dates, handle NaNs, filter rows.                   | Do it without opening the CSV in Excel.             |
| **7. EDA & Viz (Seaborn)** | Plot distributions. Find outliers. Write a paragraph explaining WHY.         | A chart without a conclusion is useless.            |
| **8. Probability & Stats** | Generate a Normal Distribution in code. Calculate Z-scores for your data.    | Use `scipy` to prove if two columns are correlated. |

🔥 **Capstone 2 — The "Automated Analyst"**

> A script that takes ANY raw CSV and generates a full report.
>
> - **Ingest:** `pd.read_csv()` on a generic file
> - **Clean:** Auto-fill missing values with column mean (using OOP skills from Phase 0)
> - **Visual:** Generate a `.png` histogram for every numeric column
> - **Stats:** Log the "Skewness" of every column to a file

📁 **Folder:** `Phase 1/`

---

### 🤖 Phase 2 — Machine Learning _(Weeks 10–18)_

**Goal:** Predict the future.
**Focus:** Scikit-Learn, Algorithms, Feature Engineering.

| Topic                             | The Real Task                                                 | Retention Check                                  |
| --------------------------------- | ------------------------------------------------------------- | ------------------------------------------------ |
| **9. Linear/Logistic Regression** | Predict Housing Prices. Predict Diabetes.                     | Plot the Decision Boundary or Regression Line.   |
| **10. Trees & Forests**           | Visualize a single Decision Tree. Then train a Random Forest. | Compare accuracy. Why did RF win? Write it down. |
| **11. Boosting (XGBoost)**        | The holy grail of tabular data. Tune hyperparameters.         | Beat your Random Forest score.                   |
| **12. Unsupervised (K-Means)**    | Cluster customers based on spending.                          | Visualize the clusters in 2D using PCA.          |
| **13. Evaluation Metrics**        | Implement Precision/Recall manually.                          | Don't just trust `accuracy_score`.               |

🔥 **Capstone 3 — The "Streamlit Predictor"**

> Your first web app.
>
> - **Model:** Train an XGBoost model on the Titanic or Heart Disease dataset
> - **Pipeline:** Use `sklearn.pipeline` to bundle cleaning + modelling
> - **UI:** Build a Streamlit app with sliders for user input and a "Predict" button
> - **Deployment:** Run locally. _(Bonus: deploy to Streamlit Cloud)_

📁 **Folder:** `Phase 2/` _(coming soon)_

---

### 🧠 Phase 3 — Deep Learning _(Weeks 19–22)_

**Goal:** Beyond tabular data. Understanding complexity.
**Focus:** PyTorch, Neural Nets. _(We switch to PyTorch here — it is the language of Research and Robotics.)_

| Topic                       | The Real Task                                           | Retention Check                                 |
| --------------------------- | ------------------------------------------------------- | ----------------------------------------------- |
| **14. Tensors & Gradients** | Manual Backpropagation (Micrograd style).               | Understand `requires_grad=True`.                |
| **15. ANN — The Basics**    | Build a Feed-Forward net for MNIST (Digit recognition). | Plot the Loss Curve over epochs.                |
| **16. Optimization**        | SGD vs Adam. Experiment with Learning Rates.            | Break the model (make it diverge), then fix it. |

🔥 **Capstone 4 — The "Digit Recognizer" from Scratch**

> Build a neural network **without** a high-level API wrapper first, then rebuild it properly with `PyTorch nn.Module`.

📁 **Folder:** `Phase 3/` _(coming soon)_

---

### 🗣️ Phase 4 — NLP _(Weeks 23–30)_

**Goal:** Teaching machines to read.
**Focus:** Text, RNNs, Transformers.

| Topic                | The Real Task                             | Retention Check                                    |
| -------------------- | ----------------------------------------- | -------------------------------------------------- |
| **17. Embeddings**   | Word2Vec. Visualizing words in 3D space.  | Find the closest word to "King" − "Man" + "Woman". |
| **18. RNN/LSTM/GRU** | Text Classification (Sentiment Analysis). | Why does Vanishing Gradient happen? Simulate it.   |
| **19. Transformers** | The Attention Mechanism. HuggingFace.     | Fine-tune BERT on a custom dataset.                |

🔥 **Capstone 5 — The "Context Chatbot"**

> A bot that answers questions based on a PDF you upload.
>
> - **Tech:** HuggingFace Transformers + FAISS (Vector DB)
> - **Task:** RAG (Retrieval Augmented Generation)

📁 **Folder:** `Phase 4/` _(coming soon)_

---

### 👁️ Phase 5 — Computer Vision _(Weeks 31–38)_

**Goal:** Teaching machines to see.
**Focus:** CNNs, Images, Object Detection. _(This is the bridge to Robotics.)_

| Topic                     | The Real Task                                                    | Retention Check                                      |
| ------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| **20. CNNs**              | Build a ConvNet for CIFAR-10 (Image classification).             | Visualize the "Feature Maps" (what the filter sees). |
| **21. Transfer Learning** | Use ResNet50. Fine-tune it to classify "Hot Dog vs Not Hot Dog". | Freeze layers vs Unfreeze layers.                    |
| **22. Object Detection**  | YOLO (You Only Look Once). Detect cars in video.                 | Draw bounding boxes in real-time.                    |

🔥 **Capstone 6 — The "Vision Security System"**

> Webcam integration with real-time detection.
>
> - **Input:** OpenCV reads webcam feed
> - **Model:** YOLOv8 detects "Person"
> - **Logic:** If "Person" detected, log timestamp to SQLite _(using Phase 0 skills!)_

📁 **Folder:** `Phase 5/` _(coming soon)_

---

### 🤖 Final Frontier — Robotics Prep

**Goal:** Apply everything to the physical world.

- **ROS2** (Robot Operating System) — The middleware of robotics
- **SLAM** — Simultaneous Localization and Mapping
- **Reinforcement Learning** — Teaching a robot to walk (simulated)

---

## ⚠️ The "Senior Dev" Retention Protocols

> These rules apply to **every single day** of the journey:

1. **The 20-Minute Rule** — Stuck? Debug for 20 minutes. Read the error. Print the variables. _Then_ ask AI.
2. **Spiral Learning** — Every project must use a **database** (Phase 0 skill) and a **visualization** (Phase 1 skill). Never drop the basics.
3. **Code Reviews** — Once a week, ask ChatGPT: _"Roast my code. Tell me why it is not production ready."_ Then fix it.

---

---

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
