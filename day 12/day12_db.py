import logging
import sqlite3
import os
import datetime
from exceptions import InvalidDataError



class DatabaseManager:
    def __init__(self, db_name = os.path.join(os.path.dirname(__file__), "app_data.db")):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self._connect()
        self._create_table()



    #function to connect to the db
    def _connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            logging.info(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            logging.critical(f"Database connection failed: {e}")
            raise InvalidDataError(e)


    #function to create the table
    def _create_table(self):
        query = """
            create table if not exists processed_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            result_type TEXT,
            value REAL
        )
        """
        self.cursor.execute(query)
        self.connection.commit()

    #function to save the results
    def save_result(self, result_type, value):
        query = "insert into processed_data (timestamp, result_type, value) values(?, ?, ?)"
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(query, (current_time,result_type, value))
        self.connection.commit()

    #function to fetch the saved data
    def fetch_all_results(self):
        query = "select * from processed_data"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    # function to delete all records (for testing purposes)

    def delete_all_results(self):
        query = "delete from processed_data"
        self.cursor.execute(query)
        self.connection.commit()

    #function to safely close the database connection.
    
    def close(self):
        try:
            if self.connection:
                self.connection.close()
                logging.info("Database connection closed.")  
        except sqlite3.Error as e:
            logging.critical(f"Database connection closure failed: {e}")
            raise InvalidDataError(e)
