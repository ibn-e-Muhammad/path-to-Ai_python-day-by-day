import logging
import sqlite3
from exceptions import InvalidDataError


class DatabaseHandler:
    def __init__(self, db_name="LifeLogger_db"):
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
                        create table if not exists LifeLogger_Data(
                                    id Integer Primary Key,
                                    Topic Text,
                                    Time float,
                                    Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                    )
''')
                self.connection.commit()
                logging.info("Table 'LifeLogger_Data' is ready.")
            except InvalidDataError as e:
                logging.critical(f"Table creation failed. Error: {e}")
                raise

#Insert data

    def Insert_data(self, topic, time):
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

#output stored data

    def display_data(self):
        if self.connection:
            try:
                self.cursor.execute('''
                    select * from LifeLogger_Data
''')
                rows = self.cursor.fetchall()
                for row in rows:    
                    print(f"ID: {row[0]}, Topic: {row[1]}, Time: {row[2]}, Date: {row[3]}")
                logging.info("Displayed all data from 'LifeLogger_Data' table.")
            except Exception as e:
                logging.error(f"Failed to retrieve data: {e}")
                raise


#close connection

    def close(self):
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")