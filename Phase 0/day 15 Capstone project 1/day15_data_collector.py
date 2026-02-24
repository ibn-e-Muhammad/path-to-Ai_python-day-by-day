import logging
from exceptions import InvalidDataError
from day15_database_methods import DatabaseHandler


class DataCollector():
    def __init__(self):
        self.topic = ""
        self.time = 0


    #taking input from user
    def collect_data(self):
        self.topic = input("What topic did you spend your time and mind on today? >> ")
        try:
            self.time = float(input(f"How many hours did you spend on {self.topic} today? >> "))
            if self.time < 0:
                logging.error("Negative time entered.")
                raise InvalidDataError("Time cannot be negative.")
            return self.topic, self.time
        except ValueError as e:
            logging.error(f"Invalid numeric input for time: {e}.")
            raise InvalidDataError("Time must be a valid numeric value.") from e


    
     
    # Input data to db file 
    def data_entry(self):
        db_pointer = DatabaseHandler()
        db_pointer.Insert_data(self.topic, self.time)
        db_pointer.close()
    # Output stored data from db file
    def display_stored_data(self):
        db_pointer = DatabaseHandler()
        db_pointer.display_data()
        db_pointer.close()