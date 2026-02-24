# Day 12: Database Integration

## Overview

This folder contains the code for Day 12, focusing on persistent data storage using SQLite.

## Key Concepts Covered

- **SQLite Database**:
  - Connecting to a local database (`app_data.db`) using the `sqlite3` library.
  - Creating tables with specific schemas (`processed_data`).
  - executing SQL queries (`INSERT`, `SELECT`, `DELETE`).
- **Database Manager Class**: Encapsulating all database interactions within a `DatabaseManager` class to keep the code organized and secure.
- **Data Persistence**: Saving the results of data processing (e.g., averages) to the database so they survive after the program exits.
- **Timestamps**: detailed timestamps `datetime` to track when data was saved.
- **Resource Management**: Properly closing database connections to prevent memory leaks.

## Code Files

- `day12_db.py`: The `DatabaseManager` class handling all SQL operations.
- `day12_main.py`: Integrating the database with the data processing logic.
- `day12_processors.py`: The data processing logic (imported from previous days).
