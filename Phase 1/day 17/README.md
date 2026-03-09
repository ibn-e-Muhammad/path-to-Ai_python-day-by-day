# Day 17: Pandas Practice + LifeLogger Integration

## Overview

Day 17 has two parts. First: 6 structured Pandas assignments covering the full DataFrame workflow — from creation to time series analysis. Second: taking everything learned (Pandas and NumPy) and integrating it directly into the **LifeLogger** project built back in Phase 0. The `DatabaseHandler` class was upgraded to load data with Pandas, compute stats with NumPy, and produce per-topic breakdowns with `groupby`. This marks the end of the standalone Python/data practice — it all lives inside real code now.

---

## Key Concepts Covered

### 1. DataFrame Creation and Indexing

- Building DataFrames from dictionaries of NumPy arrays
- Setting a column as the index: `df.set_index('col1', inplace=True)`
- Setting custom string labels as the index: `df.index = ['X', 'Y', 'Z']`
- Accessing a specific cell by label: `df['B']['Y']`

### 2. DataFrame Operations

- Adding a derived column: `df['Product'] = df['a'] * df['b']`
- Axis-wise sums: `df.sum(axis=0)` for column totals, `df.sum(axis=1)` for row totals — same `axis` convention as NumPy

### 3. Data Cleaning

- Manually introducing `NaN` values with `df.loc[row, col] = np.nan`
- Filling missing values with column means: `df['a'].fillna(df['a'].mean()).astype(int)`
- Dropping rows that contain any NaN: `df.dropna()`
- Key insight: once NaNs are introduced, the column dtype becomes `float64` — `astype(int)` is needed to restore integer types after filling

### 4. Data Aggregation (GroupBy)

- Grouping by a categorical column: `df.groupby('Category')`
- Computing multiple aggregations at once: `.agg(['sum', 'mean'])`
- Computing total sales per category: `df.groupby('Category')['Sales'].sum()`

### 5. Merging and Concatenating DataFrames

- `pd.merge(df1, df2, on='Category', how='inner')` — joins rows that share a common key, similar to SQL `JOIN`
- `pd.concat([df1, df2], axis=0)` — stacks DataFrames vertically (row-wise); columns not shared by both get filled with `NaN`
- `pd.concat([df1, df2], axis=1)` — places DataFrames side by side (column-wise)

### 6. Time Series Analysis

- Creating a datetime index with `pd.date_range(start='2024-01-01', periods=365, freq='D')`
- **Resampling**: `df.resample('ME').mean()` — collapses daily data down to monthly averages (one row per month-end)
- **Rolling window**: `df.rolling(window=7).mean()` — computes a 7-day moving average; first 6 rows are `NaN` since there aren't enough preceding days to fill the window yet

---

## LifeLogger Integration

After the practice assignments, Pandas and NumPy were integrated directly into the LifeLogger project. Key upgrades made to `day17_database_methods.py`:

- **`pd.read_sql_query()`** — fetches the entire `LifeLogger_Data` table from SQLite straight into a DataFrame instead of raw tuple lists
- **`np.sum()` / `np.mean()`** — computes total hours logged and average time per session from the `Time` column as a NumPy array
- **`df.groupby('Topic')['Time'].sum()`** — aggregates time spent per topic and prints a clean per-topic summary

The rest of the project architecture (OOP classes, logging, custom exceptions, SQLite) carries over unchanged from Phase 0 — this day just upgraded the data-handling layer to use proper Pandas/NumPy tooling.

---

## Closing Note

> _"Done with what one would need to practice to get familiar with the working of Pandas and not mess up the logic or freak out when you don't understand the code your AI gave you. The rest is that you can take help from the AI but always know what you are doing and what your code is also doing."_

---

## Code Files

- `practice.ipynb`: All 6 Pandas assignments with full outputs
- `day17_main.py`: Entry point — orchestrates data collection and display
- `day17_data_collector.py`: `DataCollector` class — CLI input, validation, and DB writes
- `day17_database_methods.py`: `DatabaseHandler` class — upgraded with Pandas/NumPy for data retrieval and stats
- `exceptions.py`: Custom exception classes
- `app.log`: Runtime log output
