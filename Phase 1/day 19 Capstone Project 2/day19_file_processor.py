import logging
import pandas as pd
import numpy as np
from pathlib import Path
from day19_report_generator import ReportGenerator

class FileProcessor:
    def __init__(self):
        self.access_file()


    def access_file(self):
        try:
            folder = Path(__file__).parent/"incoming_data"
            for file in folder.glob("*.csv"):
                self.file_path = file
                df = pd.read_csv(self.file_path)
                ReportGenerator(df)

                logging.info(f"Accessed file: {self.file_path}")
            return df
        except Exception as e:
            logging.error(f"Error occurred while accessing file: {e}")

    # def create_table(self):
    #     if self.connection:
    #         try:
    #             self.cursor.execute('''
    #                 CREATE TABLE IF NOT EXISTS LifeLogger_Data(
    #                     id INTEGER PRIMARY KEY,
    #                     Topic TEXT,
    #                     Time FLOAT,
    #                     Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #                 )
    #             ''')
    #             self.connection.commit()
    #             logging.info("Table 'LifeLogger_Data' is ready.")
    #         except Exception as e:
    #             logging.critical(f"Table creation failed. Error: {e}")
    #             raise

    # def insert_data(self, topic, time):
    #     if self.connection:
    #         try:
    #             self.cursor.execute('''
    #                 INSERT INTO LifeLogger_Data (Topic, Time, Date) VALUES (?, ?, CURRENT_TIMESTAMP)
    #             ''', (topic, time))
    #             self.connection.commit()
    #             logging.info(f"Inserted data: topic={topic}, time={time}")
    #         except Exception as e:
    #             logging.error(f"Failed to insert data: {e}")
    #             raise

    # def display_data(self):
    #     """Fetches data, prints it, and returns the Time column as a NumPy array."""
    #     if not self.connection:
    #         return np.array([])

    #     try:
    #         df = pd.read_sql_query("SELECT * FROM LifeLogger_Data", self.connection)

    #         if df.empty:
    #             print("No data found in the database.")
    #             return np.array([])

    #         # Print data for the user
    #         print(df)
    #         # Extract just the 'Time' column (index 2) into a NumPy array
    #         # We use a list comprehension because sqlite3 returns a list of tuples
    #         time_data = df["Time"]
            
    #         logging.info("Data retrieved and converted to NumPy array.")
    #         return time_data, df

    #     except Exception as e:
    #         logging.error(f"Failed to retrieve data: {e}")
    #         raise

    # def calculate_stats(self, time_array, df):
    #     """Performs calculations on the provided NumPy array."""
    #     if time_array.size == 0:
    #         print("No data available to calculate stats.")
    #         return

    #     total_sum = np.sum(time_array)
    #     average_time = np.mean(time_array)

    #     print("\n--- Statistics ---")
    #     print(f"Total Time Logged: {total_sum:.2f}")
    #     print(f"Average Time per Entry: {average_time:.2f}")
    #     time_per_topic = df.groupby("Topic")["Time"].sum()
    #     print(f"Total Time spent per topic: \n{time_per_topic}")
        
    #     return total_sum, average_time
    
    # def close(self):
    #     if self.connection:
    #         self.connection.close()
    #         logging.info("Database connection closed.")

    