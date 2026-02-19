# Day 14: Database Integration and Error Handling

## Overview

This folder contains the code for Day 14, where the processing logic is fully integrated with database operations to create a complete data pipeline.

## Key Concepts Covered

- **Database Handler**: A dedicated `DatabaseHandler` class to manage SQLite connections, table creation, and data insertion.
- **Data Pipeline**: The flow of data from input -> validation -> processing -> storage.
- **Exception handling**: specific error handling for database connection and query execution failures.
- **Logging**: Extensive logging of database events (successes and failures) for debugging.
- **Data Persistence**: Storing calculated statistics (positives, average, min, max) into the `Processed_Data` table.

## Code Files

- `day14_database_methods.py`: Handles all SQL interactions.
- `day14_processors.py`: Processes data and triggers database saves.
- `day14_main.py`: Orchestrates the flow.
