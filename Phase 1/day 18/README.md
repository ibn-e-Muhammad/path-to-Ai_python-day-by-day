# Day 18: Visualization — Matplotlib & Seaborn

## Overview

Day 18 covers the visualization chapter. The focus is on getting comfortable with both **Matplotlib** and **Seaborn**, moving from base plots on a sales CSV to advanced statistical plotting on Seaborn's built-in `tips` dataset. By the end of this practice, we covered 9 different plot types: line plots, bar charts, histograms, scatter plots, KDE plots, box plots, violin plots, pair plots, and correlation heatmaps.

---

## Key Concepts Covered

### 1. Loading & Preparing Data for Plotting

- Reading a CSV into a DataFrame (`pd.read_csv`) and a built-in Seaborn dataset (`sns.load_dataset('tips')`)
- Aggregating for plotting: `df.groupby(...)[...].sum().reset_index()`
- The `reset_index()` call turns the groupby result back into a proper flat DataFrame — necessary when you want to pass columns directly to a plot.

### 2. Matplotlib Fundamentals

- **Line Plot (`plt.plot()`)**: Basic charting mapping categories to values.
- **Bar Chart (`plt.bar()`)**: Vertical bars comparing groups, with rotated x-axis labels (`plt.xticks(rotation=30)`) to prevent overlap. Used `xlabel`, `ylabel`, and `title` to label graphs clearly.
- **Histogram (`plt.hist()`)**: Visualizing distributions using custom bins.
- **Scatter Plot (`plt.scatter()`)**: Mapping data as individual points, customized with marker shapes (`marker="*"`) and colors.

### 3. Seaborn Statistical Plotting

- **Relational Plots**: Recreated scatter plots (`sns.scatterplot`) and line plots (`sns.lineplot`) using Seaborn's cleaner API mapped directly to DataFrame column names (e.g., `x="size", y="total_bill", data=tips`).
- **Categorical Distributions**:
  - **Bar Plot (`sns.barplot`)**: Automatically handles grouped calculations with error bars.
  - **Box Plot (`sns.boxplot`)**: Identifying outliers and quartiles for tipping across different days.
  - **Violin Plot (`sns.violinplot`)**: Combining a box plot with a kernel density output to show the shape of the data grouped by category (e.g., tip sizes by `sex`).
- **Continuous Distributions**:
  - **Histplot (`sns.histplot`)**: Layered frequency bars with an optional KDE line overlay (`kde=True`).
  - **KDE Plot (`sns.kdeplot`)**: Filled kernel density estimation plots.
- **Multi-Variable Analytics**:
  - **Pair Plot (`sns.pairplot()`)**: Automatically creating a grid of scatter plots comparing every numerical column against each other.
  - **Heatmap (`sns.heatmap()`)**: Visualizing the correlation matrix (`df.corr()`) of numerical variables with text annotations (`annot=True`) to immediately see the strength of relationships.

---

## Code Files

- `practice.ipynb`: Matplotlib & Seaborn practice — data loading, groupby, and 9 different chart types.
- `sample_data/sales_data.csv`: Real-world sales dataset used for matplotlib plots.
