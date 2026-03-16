# Phase 1 — The Data Mechanic (Day 16+)

> **Goal:** You cannot model what you cannot clean. Master the numerical and data tools that every ML pipeline is built on — NumPy, Pandas, visualization, and statistics.

---

## 🗺️ Phase Overview

| Day(s) | Theme               | Key Skill                                                                                               | Status      |
| ------ | ------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| Day 16 | Numerical Computing | NumPy — arrays, linear algebra, masking, implementation in LifeLogger                                   | ✅ Complete |
| Day 17 | Data Manipulation   | Pandas — DataFrames, cleaning, groupby, merging, time series + Pandas/NumPy in LifeLogger               | ✅ Complete |
| Day 18 | Visualization       | Matplotlib & Seaborn — 9 plot types: line, bar, histogram, scatter, KDE, box, violin, pairplot, heatmap | ✅ Complete |
| Day 19 | Capstone Project 2  | The Automated Analyst — full file-to-report pipeline with OOP, Pandas, NumPy, matplotlib, scipy         | ✅ Complete |

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

### Day 18 — Visualization: Matplotlib & Seaborn

**Focus:** Full visualization practice (9 chart types) using Matplotlib on a real sales CSV and Seaborn on the built-in `tips` dataset.

**Matplotlib charts:** line plot, bar chart, histogram, scatter plot — all built manually via `plt.plot/bar/hist/scatter` on aggregated `groupby` data from `sales_data.csv`.

**Seaborn charts:** scatter (`sns.scatterplot`), line (`sns.lineplot`), bar (`sns.barplot`), box (`sns.boxplot`), violin (`sns.violinplot`), histogram with KDE overlay (`sns.histplot` + `kde=True`), KDE plot (`sns.kdeplot`), pair plot (`sns.pairplot`), correlation heatmap (`sns.heatmap` on `df.corr()` with `annot=True`).

**Key insight documented:** `reset_index()` after `groupby` is required to turn the result back into a flat DataFrame so columns can be passed directly to plot functions.

📁 Folder: `day 18/`

---

### Day 19 — Capstone Project 2: The Automated Analyst 🏆

**Focus:** A complete, automated CSV-to-report pipeline combining all Phase 1 skills (Pandas, NumPy, matplotlib, scipy) with the OOP architecture from Phase 0.

**Application:** Scans `incoming_data/` for any CSV file, cleans it, generates a histogram for every numeric column, logs skewness stats, and prints a full `df.describe()` summary — all without any manual intervention.

**Key components:**

- `FileProcessor` — uses `pathlib.Path.glob('*.csv')` to dynamically find and load files
- `ReportGenerator` — 4-step constructor pipeline: `clean_data()` → `generate_histograms()` → `log_skewness()` → `report_generator()`
- `scipy.stats.skew()` — first use of `scipy` in the project
- All output (`.png` histograms, `skewness_stats.log`) saved to auto-created `reports/` directory

📁 Folder: `day 19 Capstone Project 2/`

---

## 🎯 Phase 1 Goals

Building on the complete Python foundation from Phase 0, Phase 1 targets:

| Area              | Topics to Cover                                           | Status       |
| ----------------- | --------------------------------------------------------- | ------------ |
| **NumPy**         | Arrays, linear algebra, broadcasting, masked arrays       | ✅ Done      |
| **Pandas**        | DataFrames, cleaning, groupby, merging, time series       | ✅ Done      |
| **Visualization** | `matplotlib`, `seaborn` — distributions, outliers, charts | ✅ Done      |
| **Statistics**    | Probability, Z-scores, correlations (`scipy`)             | ⬜ Coming up |
| **Capstone 2**    | The "Automated Analyst" — auto-report from any CSV        | ✅ Done      |

> This section is updated day-by-day as Phase 1 progresses.
