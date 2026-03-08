# Day 17: Introduction to Pandas — DataFrames, Cleaning, Aggregation & Time Series

## Overview

Day 17 is the first full Pandas day of Phase 1. After getting comfortable with NumPy's array model, the focus shifts to **DataFrames** — the primary data structure for everything in data science and ML. The day is structured as 6 progressive assignments, going from constructing DataFrames from scratch all the way to working with time-indexed data and rolling averages. This wraps up the Python practice phase — next step is implementing it all in a real project.

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

## Closing Note

This wraps up the structured Python/Pandas practice portion. The goal from here is to take everything learned — NumPy arrays, DataFrame operations, cleaning, groupby, time series — and plug it into the real project built during Phase 0.

> _"Done with what one would need to practice to get familiar with the working of Pandas and not mess up the logic or freak out when you don't understand the code your AI gave you. The rest is that you can take help from the AI but always know what you are doing and what your code is also doing."_

---

## Code Files

- `practice.ipynb`: All 6 Pandas assignments with full outputs
