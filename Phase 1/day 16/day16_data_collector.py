import logging
from exceptions import InvalidDataError
from day16_database_methods import DatabaseHandler


class DataCollector():
    def __init__(self):
        self.topic = ""
        self.time = 0
        self.db_pointer = DatabaseHandler()


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
        self.db_pointer.insert_data(self.topic, self.time)
    # Output stored data from db file
    def display_stored_data(self):
        time_array = self.db_pointer.display_data()
        self.db_pointer.calculate_stats(time_array)
        self.db_pointer.close()