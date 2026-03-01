import logging
import sqlite3
import numpy as np

class DatabaseHandler:
    def __init__(self, db_name="LifeLogger_db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_table()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            logging.info("Database successfully connected.")
        except sqlite3.Error as e:
            logging.critical(f"Failed to connect to the database: {e}")
            raise

    def create_table(self):
        if self.connection:
            try:
                self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS LifeLogger_Data(
                        id INTEGER PRIMARY KEY,
                        Topic TEXT,
                        Time FLOAT,
                        Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                self.connection.commit()
                logging.info("Table 'LifeLogger_Data' is ready.")
            except Exception as e:
                logging.critical(f"Table creation failed. Error: {e}")
                raise

    def insert_data(self, topic, time):
        if self.connection:
            try:
                self.cursor.execute('''
                    INSERT INTO LifeLogger_Data (Topic, Time, Date) VALUES (?, ?, CURRENT_TIMESTAMP)
                ''', (topic, time))
                self.connection.commit()
                logging.info(f"Inserted data: topic={topic}, time={time}")
            except Exception as e:
                logging.error(f"Failed to insert data: {e}")
                raise

    def display_data(self):
        """Fetches data, prints it, and returns the Time column as a NumPy array."""
        if not self.connection:
            return np.array([])

        try:
            self.cursor.execute('SELECT * FROM LifeLogger_Data')
            rows = self.cursor.fetchall()

            if not rows:
                print("No data found in the database.")
                return np.array([])

            # Print data for the user
            for row in rows:    
                print(f"ID: {row[0]}, Topic: {row[1]}, Time: {row[2]}, Date: {row[3]}")

            # Extract just the 'Time' column (index 2) into a NumPy array
            # We use a list comprehension because sqlite3 returns a list of tuples
            time_data = np.array([row[2] for row in rows], dtype=float)
            
            logging.info("Data retrieved and converted to NumPy array.")
            return time_data

        except Exception as e:
            logging.error(f"Failed to retrieve data: {e}")
            raise

    def calculate_stats(self, time_array):
        """Performs calculations on the provided NumPy array."""
        if time_array.size == 0:
            print("No data available to calculate stats.")
            return

        total_sum = np.sum(time_array)
        average_time = np.mean(time_array)

        print("\n--- Statistics ---")
        print(f"Total Time Logged: {total_sum:.2f}")
        print(f"Average Time per Entry: {average_time:.2f}")
        
        return total_sum, average_time
    
    def close(self):
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

    