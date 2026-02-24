import logging
import statistics # We will use this for median
from day10_processors import DataProcessor
from exceptions import InvalidDataError

# 1. THE INHERITANCE
class AdvancedDataProcessor(DataProcessor):
    """
    A specialized version of DataProcessor for financial/scientific data.
    It inherits EVERYTHING from DataProcessor (init, count_positive, etc.)
    """
    
    def __init__(self, data, dataset_name="Default"):
        super().__init__(data)
        self.dataset_name = dataset_name
        logging.info(f"Advanced Processor started for: {self.dataset_name}")

    # 3. OVERRIDING A METHOD
    def safe_average(self):
        if not self.data:
            logging.error(f"Cannot average empty dataset: {self.dataset_name}")
            raise InvalidDataError("Dataset is empty! Cannot calculate average.")
        return super().safe_average()
    
    # 4. EXTENDING (New Method)

    def calculate_median(self):
        if not self.data:
            return None
        else:
            return statistics.median(self.data)