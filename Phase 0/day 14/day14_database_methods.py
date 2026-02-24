import logging
import sqlite3
from exceptions import InvalidDataError


class DatabaseHandler:
    def __init__(self, db_name="processedData_db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_table()

#connect

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            logging.info("Database successfully connected.")
        except:
            logging.critical("Failed to connect to the database.")
            raise

#create table
    def create_table(self):
        if self.connection:
            try:
                self.cursor.execute('''
                        create table if not exists Processed_Data(
                                    id Integer Primary Key,
                                    Positives Integer,
                                    Average float,
                                    Min Integer,
                                    Max Integer
                                    )
''')
                self.connection.commit()
                logging.info("Table 'Processed_Data' is ready.")
            except InvalidDataError as e:
                logging.critical(f"Table creation failed. Error: {e}")
                raise

#Insert data

    def Insert_data(self, positives, average, min_val, max_val):
        if self.connection:
            try:
                self.cursor.execute('''
                    INSERT INTO Processed_Data (Positives, Average, Min, Max) VALUES (?, ?, ?, ?)
                ''', (positives, average, min_val, max_val))
                self.connection.commit()
                logging.info(f"Inserted data: positives={positives}, avg={average}, min={min_val}, max={max_val}")
            except Exception as e:
                logging.error(f"Failed to insert data: {e}")
                raise

#output stored data

    def display_data(self):
        if self.connection:
            try:
                self.cursor.execute('''
                    select * from Processed_Data
''')
                rows = self.cursor.fetchall()
                for row in rows:    
                    print(f"ID: {row[0]}, Positives: {row[1]}, Average: {row[2]}, Min: {row[3]}, Max: {row[4]}")
                logging.info("Displayed all data from 'Processed_Data' table.")
            except Exception as e:
                logging.error(f"Failed to retrieve data: {e}")
                raise


#close connection

    def close(self):
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")