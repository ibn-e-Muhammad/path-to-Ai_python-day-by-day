# Phase 1 — The Data Mechanic (Day 16+)

> **Goal:** You cannot model what you cannot clean. Master the numerical and data tools that every ML pipeline is built on — NumPy, Pandas, visualization, and statistics.

---

## 🗺️ Phase Overview

| Day(s) | Theme               | Key Skill                                                                                 | Status      |
| ------ | ------------------- | ----------------------------------------------------------------------------------------- | ----------- |
| Day 16 | Numerical Computing | NumPy — arrays, linear algebra, masking, implementation in LifeLogger                     | ✅ Complete |
| Day 17 | Data Manipulation   | Pandas — DataFrames, cleaning, groupby, merging, time series + Pandas/NumPy in LifeLogger | ✅ Complete |
| Day 18 | Visualization       | Matplotlib & Seaborn — distributions, relational & categorical plots, heatmaps            | ✅ Complete |
| Day 19 | Capstone Project 2  | The Automated Analyst — auto-report pipeline scanning for CSV data                        | ✅ Complete |

---

## 📅 Day-by-Day Breakdown

### Day 16 — NumPy: Arrays, Operations & Linear Algebra

**Focus:** Shifted from software engineering (Phase 0) to numerical computing. Completed 10 structured NumPy assignments covering the full range of array operations.

**Topics:** Array creation & manipulation, indexing & slicing, element-wise operations, statistical ops & Z-score normalization, broadcasting, linear algebra (`linalg.det`, `inv`, `eig`), reshape/flatten, fancy & boolean indexing, structured arrays, masked arrays (`numpy.ma`).

📁 Folder: `day 16/`

---

### Day 17 — Pandas: DataFrames, Cleaning, Aggregation & Time Series + LifeLogger Integration

**Focus:** Full Pandas practice (6 assignments) followed by integrating Pandas and NumPy directly into the LifeLogger project built in Phase 0.

**Practice topics:** DataFrame creation & custom indexing, derived columns & axis-wise sums, data cleaning (`fillna`, `dropna`), groupby aggregation, merging & concatenating DataFrames, time series with datetime indexes, `resample()` for monthly means, `rolling()` for 7-day averages.

**Implementation:** The LifeLogger `DatabaseHandler` was upgraded to use `pd.read_sql_query()` to load stored sessions into a DataFrame, `np.sum()`/`np.mean()` to compute total and average time logged, and `df.groupby('Topic')['Time'].sum()` to break down time spent per topic.

📁 Folder: `day 17/`

---

### Day 18 — Matplotlib & Seaborn: Real Data & Statistical Plotting

**Focus:** Getting hands-on with data visualization pipelines using `matplotlib` and `seaborn`.

**Topics:** Loading & grouping sales data with Pandas to visualize with Matplotlib `plot`, `bar`, `hist`, and `scatter`. Loading the seaborn `tips` dataset to generate statistical visualizations natively: `scatterplot`, `lineplot`, `barplot`, `boxplot`, `violinplot`, `histplot`, `kdeplot`, `pairplot`, and a correlation `heatmap`.

📁 Folder: `day 18/`

---

### Day 19 — Capstone Project 2: The Automated Analyst

**Focus:** Applying Python file handling and data analysis skills to build an automated application.

**Topics:** Programmatically using `pathlib` to scan an `incoming_data/` directory for raw CSVs. Orchestrating a pipeline where a `FileProcessor` ingests the data into Pandas DataFrames and a `ReportGenerator` calculates and logs statistical descriptions dynamically.

📁 Folder: `day 19 Capstone Project 2/`

---

## 🎯 Phase 1 Goals

Building on the complete Python foundation from Phase 0, Phase 1 targets:

| Area              | Topics to Cover                                           | Status       |
| ----------------- | --------------------------------------------------------- | ------------ |
| **NumPy**         | Arrays, linear algebra, broadcasting, masked arrays       | ✅ Done      |
| **Pandas**        | DataFrames, cleaning, groupby, merging, time series       | ✅ Done      |
| **Visualization** | `matplotlib`, `seaborn` — distributions, outliers, charts | ✅ Done      |
| **Capstone 2**    | The "Automated Analyst" — auto-report from any CSV        | ✅ Done      |

> This section is updated day-by-day as Phase 1 progresses.
