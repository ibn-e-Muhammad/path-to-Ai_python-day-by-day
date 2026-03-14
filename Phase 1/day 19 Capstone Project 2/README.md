# Day 19: Capstone Project 2 — The Automated Analyst

## Overview

Day 19 consists of the second capstone project of the learning journey: **The Automated Analyst**. This project applies prior knowledge in Python file handling, OOP, error handling, Pandas, and NumPy to build an automated data processing pipeline. The application automatically consumes CSV files from an incoming directory, extracts meaningful analytical summaries, and handles potential errors gracefully.

---

## Key Components

### 1. `day19_main.py` (The Orchestrator)

- Configures centralized logging to `app.log` at the `DEBUG` level.
- Serves as the main entry point to initiate the data processing sequence by instantiating `FileProcessor`.

### 2. `day19_file_processor.py` (The Data Ingestor)

- Uses the `pathlib` module to programmatically scan the `incoming_data/` directory.
- Dynamically globs `*.csv` files, reading each into a Pandas DataFrame using `pd.read_csv()`.
- Catches and logs exceptions (e.g., file not found, permission errors) to keep the pipeline stable.
- Passes valid DataFrames directly to the `ReportGenerator` class for analysis.

### 3. `day19_report_generator.py` (The Analytical Engine)

- Receives DataFrames injected by the FileProcessor.
- Uses Pandas' robust `df.describe()` method to instantly calculate summary statistics (count, mean, std, min/max, percentiles) for all numeric columns.
- Prints the generated report and logs any analytical errors that might occur during the process.

### 4. `exceptions.py`

- Custom exception handlers (e.g., `InvalidDataError`) designed to manage domain-specific failures without crashing the application.

---

## Workflow

1. A CSV file is dropped into `incoming_data/`.
2. `day19_main.py` is executed.
3. The `FileProcessor` finds the file, loads it via Pandas, and logs the action.
4. The DataFrame is handed to `ReportGenerator`, which calculates statistical profiles and displays the results.

This project reinforces how Python automation can turn manual CSV analysis into a hands-off, scalable data pipeline.
