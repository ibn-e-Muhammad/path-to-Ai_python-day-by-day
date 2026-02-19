# Day 15: Capstone Project 1 - LifeLogger

## Overview

This folder contains the code for Day 15, the first Capstone Project. The goal was to build "LifeLogger," a console application that tracks how much time you spend on different topics.

## Application Features

- **Data Collection**: Interactive CLI to ask users for a "Topic" and "Time Spent" (in hours).
- **Validation**:
  - Ensures time is a number.
  - Prevents negative time entries.
- **Persistence**: Saves every entry into a SQLite database (`LifeLogger_db`), so no data is lost when the program closes.
- **Reporting**: Displays a history of all logged activities with timestamps.

## Code Structure

- `day15_main.py`: The entry point for the application.
- `day15_data_collector.py`: Contains the `DataCollector` class to handle user input and validation.
- `day15_database_methods.py`: Manages the `LifeLogger_db` database and `LifeLogger_Data` table.
- `exceptions.py`: Custom error classes for robust error handling.
- `app.log`: Logs internal application events for debugging.
