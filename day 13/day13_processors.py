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
        print(positives)

    def count_positive(self):
        """
        Refactor your old function here.
        Rule: Return 0 if list is empty, not None.
        Rule: Log the result before returning.
        """
        # TODO: Implement logic to count positive numbers in self.data
        count = 0
        nums = self.data
        if not nums:
            logging.info("The data list is empty")
            return 0
        else:
            for num in nums:
                if num > 0:
                    count += 1
        logging.info(f"The total positive numbers are {count}")
        return count



    def safe_average(self):
        """
        Refactor your old function here.
        Rule: Handle ZeroDivisionError using try/except.
        Rule: Log an error if the list is empty/sum fails.
        """
        # TODO: Implement logic to average self.data
        nums = self.data
        if not nums:
            logging.info("The data list is empty")
            return None
        else:
            try:
                return sum(nums)/len(nums)
            except ZeroDivisionError:
                logging.error("The division failed due to zero divisor error")
                return None

    def get_extreme_values(self):
        nums = self.data
        if not nums:
            logging.warning("The list is Empty")
            return (None, None)
        else:
            return (max(nums), min(nums))   