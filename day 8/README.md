# Day 8: Modular Design and Execution Blocks

## Overview

This folder contains the code for Day 8, which emphasizes a clean, modular project structure and proper script execution points.

## Key Concepts Covered

- **Separation of Concerns**: Organizing code into distinct modules:
  - `day8_data.py`: Storing raw data.
  - `day8_utils.py`: Containing reusable logic and helper functions.
  - `day8_mian.py`: Acting as the entry point for the application.
- **Main Execution Block**: Using the `if __name__ == "__main__":` idiom to ensure code runs only when executed directly, not when imported.
- **Importing**: Importing specific variables and functions from other local modules.
- **Data Cleaning**: Iterating through a list of strings to clean and format them (removing numbers, special characters, whitespace).
- **Safe Operations**: Handling potential edge cases (like empty lists) in functions like `safe_average`.

## Code Files

- `day8_data.py`: Variables `lst` and `str_lst`.
- `day8_utils.py`: Functions `safe_average`, `clean_words`, and `count_positive`.
- `day8_mian.py`: Main script that ties everything together.
