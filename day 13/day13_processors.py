import logging
from exceptions import InvalidDataError
from day13_base_processor import BaseProcessor

class DataProcessor(BaseProcessor):

    def _validate(self, data):
        """
        Constructor: This runs when you create the object.
        self.data is now a property of the object.
        """
        if not isinstance(data, list):
            logging.critical("The data is not a list")
            raise InvalidDataError("Data must be a list")
        for item in data:
            if not isinstance(item, (int, float)):
                logging.error(f"The entered data {item} is not valid")
                raise InvalidDataError("Data must only contain numbers")
            
        self.data = data
        logging.info(f"DataProcessor initialized with {len(data)} items.")

 # --- NEW MAGIC METHODS (TODO) ---

    def __str__(self):
        return f"DataProcessor with {len(self.data)} items"
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    
 # --- Normal calculative METHODS/Method (TODO) ---
    def process(self):
        if not self.data:
            return {
                "count_positive": 0,
                "average": None,
                "min": None,
                "max": None
            }
        positives = [n for n in self.data if n > 0]
        return {
            "positives": len(positives),
            "average": sum(self.data) / len(self.data),
            "min": min(self.data),
            "max": max(self.data)
        }  