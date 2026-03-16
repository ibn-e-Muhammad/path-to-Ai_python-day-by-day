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

- Receives DataFrames injected by the `FileProcessor` and runs a 4-step sequential pipeline in `__init__`:
  1. **`clean_data(df)`** — auto-fills missing values with the column mean using `df.select_dtypes(include=[np.number])` to target only numeric columns, then `fillna(column_mean)` for any column with nulls.
  2. **`generate_histograms(df)`** — iterates over every numeric column via `select_dtypes()` and saves a labelled `.png` histogram (using `matplotlib.pyplot`) to the auto-created `reports/` directory.
  3. **`log_skewness(df)`** — computes the skewness of every numeric column using `scipy.stats.skew()` and writes a formatted `skewness_stats.log` file to `reports/`.
  4. **`report_generator(df)`** — uses `df.describe()` to print a full summary statistics table (count, mean, std, min/max, percentiles) for all numeric columns to the console.
- The `reports/` output directory is auto-created at startup using `pathlib.Path.mkdir(exist_ok=True)`, so no manual setup is needed.

### 4. `exceptions.py`

- Custom exception handlers (e.g., `InvalidDataError`) designed to manage domain-specific failures without crashing the application.

---

## Workflow

1. A CSV file is dropped into `incoming_data/`.
2. `day19_main.py` is executed.
3. `FileProcessor` globs all `*.csv` files from `incoming_data/`, loads each with `pd.read_csv()`, and passes each DataFrame to `ReportGenerator`.
4. `ReportGenerator` runs its 4-step pipeline automatically on construction:
   - **Clean**: fills NaN cells in numeric columns with column means.
   - **Histograms**: saves a `.png` per numeric column to `reports/`.
   - **Skewness**: logs per-column skewness values (via `scipy.stats.skew()`) to `reports/skewness_stats.log`.
   - **Report**: prints the full `df.describe()` summary statistics to the console.

All events are logged to `app.log` at the `DEBUG` level throughout the entire pipeline.

---

## Key Libraries Used

| Library       | Usage                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------- |
| `pandas`      | `pd.read_csv()`, `df.describe()`, `select_dtypes()`, `fillna()`                           |
| `numpy`       | `np.number` dtype selector for numeric column filtering                                   |
| `matplotlib`  | `plt.hist()`, `plt.savefig()` — histogram generation                                      |
| `scipy.stats` | `stats.skew()` — skewness calculation per column                                          |
| `pathlib`     | `Path` for cross-platform file paths; `mkdir(exist_ok=True)` for auto-creating `reports/` |

---

## Output Files

- `reports/histogram_<column_name>.png` — one histogram image per numeric column
- `reports/skewness_stats.log` — formatted skewness report for all numeric columns
- `app.log` — full debug-level runtime log of the pipeline

This project reinforces how Python automation can turn manual CSV analysis into a hands-off, scalable data pipeline.
