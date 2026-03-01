# Day 16: Introduction to NumPy — Arrays, Operations & Linear Algebra

## Overview

This is the first day of **Phase 1**. The focus shifts from building software infrastructure (Phase 0) to numerical computing — the backbone of all data science and ML work. The day is structured as 10 progressive assignment problems using **NumPy**, covering everything from basic array creation to masked arrays and linear algebra. The `.py` files carry the LifeLogger project forward from Phase 0 as the main project base.

---

## Key Concepts Covered

### 1. Array Creation and Manipulation

- Creating arrays with `np.random.randint()`, `np.arange()`, and `reshape()`
- Column-wise assignment using slice notation: `arr[:, 2] = 1`
- Zeroing out diagonal elements with `np.fill_diagonal()`

### 2. Indexing and Slicing

- Extracting sub-arrays using row/column ranges: `arr[2:5, 1:4]`
- Extracting border elements using `np.concatenate()` on edge slices
- Understanding 0-based vs positional indexing

### 3. Element-wise Array Operations

- Standard arithmetic between same-shape arrays: `+`, `-`, `*`, `/` — all element-wise by default in NumPy (no loops needed)
- Axis-based aggregation: `np.sum(arr, axis=0)` for column sums, `axis=1` for row sums

### 4. Statistical Operations

- Core stats on arrays: `np.mean()`, `np.median()`, `np.std()`, `np.var()`
- **Normalization (Z-score scaling)**: `(arr - mean) / std_dev` — scales values to mean=0, std=1. This is a pattern you'll see in almost every ML preprocessing pipeline.

### 5. Broadcasting

- NumPy's broadcasting lets you perform operations between arrays of _different shapes_ without explicit loops
- Adding a 1D array `(3,)` to a 2D array `(3, 3)` — NumPy automatically "broadcasts" the 1D array across each row
- Subtracting column-wise by reshaping or using compatible shapes

### 6. Linear Algebra (`numpy.linalg`)

- `np.linalg.det()` — matrix determinant
- `np.linalg.inv()` — matrix inverse
- `np.linalg.eig()` — eigenvalues and eigenvectors (returns complex numbers for non-symmetric matrices)
- Matrix multiplication with `.dot()` — shape `(2,3) · (3,2)` → `(2,2)`

### 7. Advanced Array Manipulation

- `reshape()` to change array dimensions without changing data: `(3,3)` → `(1,9)` → `(9,1)`
- `flatten()` to collapse any N-D array into a 1D array, then reshape it back

### 8. Fancy Indexing and Boolean Indexing

- **Fancy indexing**: using arrays of indices to select specific elements — e.g., extracting the 4 corner elements of a matrix
- **Boolean indexing**: using a condition as a mask to filter or replace values — e.g., `arr[arr > 10] = 10` caps all values at 10 in-place

### 9. Structured Arrays

- Creating arrays with **named, typed fields** using `dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]`
- Sorting structured arrays by a specific field: `arr.sort(order='age')`
- Computing **Euclidean distance** between 2D coordinate points using `np.newaxis` for broadcasting: `sqrt((x1-x2)² + (y1-y2)²)`

### 10. Masked Arrays (`numpy.ma`)

- `ma.masked_greater(array, 10)` — hides elements above a threshold, while keeping the array shape intact
- `ma.masked_array(array, mask=np.eye(3, dtype=bool))` — masks diagonal elements
- `masked_array.sum()` — operates only on visible (unmasked) elements
- `masked_array.filled(value)` — fills masked positions with a given value (e.g., the mean of unmasked elements)

---

## Honest Note

Assignment 10 (Masked Arrays) required AI help — the `numpy.ma` API has many specialized functions that aren't intuitive on first encounter. The key takeaway noted in the notebook:

> _"Google stuff first, try to solve it and learn it first, then just use AI. This way you'd know what is going on with your code even when you're 'vibe coding'."_

---

## Code Files

- `practice.ipynb`: All 10 NumPy assignments with outputs
- `day16_main.py`: LifeLogger entry point (carried over from Phase 0)
- `day16_data_collector.py`: `DataCollector` class for user input and validation
- `day16_database_methods.py`: SQLite database handler for LifeLogger logging
- `exceptions.py`: Custom exception classes for the project
- `app.log`: Runtime log output from the LifeLogger application
