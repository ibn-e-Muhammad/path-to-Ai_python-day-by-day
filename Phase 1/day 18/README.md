# Day 18: Visualization — Matplotlib _(In Progress)_

## Overview

Day 18 is the start of the visualization chapter. The plan is to cover both **Matplotlib** and **Seaborn** — but Seaborn hasn't been touched yet. So far, this day is all about getting comfortable with `matplotlib.pyplot` using a real-world sales dataset (`sales_data.csv`). Instead of generating random numbers, actual CSV data was loaded with Pandas, aggregated with `groupby`, and then plotted four different ways to see what sticks visually.

---

## Key Concepts Covered (so far)

### 1. Loading & Preparing Data for Plotting

- Reading a CSV into a DataFrame: `pd.read_csv('sample_data/sales_data.csv')`
- Inspecting data with `.head()` and `.info()` before doing anything with it
- Aggregating for plotting: `df.groupby('Product Category')['Total Revenue'].sum().reset_index()`
- The `reset_index()` call turns the groupby result back into a proper flat DataFrame — necessary when you want to pass columns directly to a plot

### 2. Line Plot (`plt.plot()`)

- Basic line chart mapping categorical product categories to their total revenue
- Useful for spotting trends across ordered categories

### 3. Bar Chart (`plt.bar()`)

- `plt.bar(x, y, color='teal')` — vertical bars comparing revenue across product categories
- `plt.xticks(rotation=30)` — rotated x-axis labels so the category names don't overlap
- Added proper axis labels with `plt.xlabel()`, `plt.ylabel()`, and a descriptive `plt.title()`

### 4. Histogram (`plt.hist()`)

- `plt.hist(data, color='pink', bins=10)` — shows the distribution of revenue values across the bins
- Useful for understanding the spread and frequency of data rather than comparing categories

### 5. Scatter Plot (`plt.scatter()`)

- `plt.scatter(x, y, color='teal', marker='*')` — maps categories to revenue as individual points with a custom star marker
- `plt.xticks(rotation=30)` again to handle the label overlap on the x-axis

---

## What's Next

- **Seaborn** — distributions (`histplot`, `kdeplot`), relationships (`scatterplot`, `pairplot`), and categorical summaries (`boxplot`, `violinplot`)
- More plot customization: figure sizing, subplots, legends, and styling

---

## Code Files

- `practice.ipynb`: Matplotlib practice — data loading, groupby, and 4 chart types on sales data
- `sample_data/sales_data.csv`: Real-world sales dataset used for all plots
