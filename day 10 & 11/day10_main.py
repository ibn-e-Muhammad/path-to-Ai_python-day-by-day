import logging
import os
# We import our classes from the other files
from day10_processors import DataProcessor
from day10_cleaners import TextCleaner
from exceptions import InvalidDataError
from day10_advanced_processors import AdvancedDataProcessor

# 1. SETUP LOGGING
# This configures logging for the ENTIRE application
logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), "app.log"), 
    level=logging.DEBUG,  # Changed to DEBUG to capture all levels
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='w',
)

def main():
    # Test Data (Simulating inputs)
    test_inputs = [
    [1, 2, 3],
    [],
    [1, "a", 3],
    "123",
    ["123  !  ", "abc"],
    [0, -1, 2, 3, -5, 8, -13, 21],
    ["@ali", "  HiNa!!!", "  *baZooka##  "]
    ]
    

    print("--- Starting Processing ---")

    # 1. Test Number Processor
    for data in test_inputs:
        try:
            processor = DataProcessor(data)
            adv_processor = AdvancedDataProcessor(data)
            # Note: We are printing to console for user, but the Class logs internally too!
            print(processor)  # Using __str__ method
            print(f"Length: {len(processor)}")  # Using __len__ method
            print(f"First item: {processor[0]}")  # Using __getitem__ method
            print(f"Positives: {processor.count_positive()}")
            print(f"Average: {processor.safe_average()}")
            print(f"The Min value: {processor.get_extreme_values()[1]}")
            print(f"The Max value: {processor.get_extreme_values()[0]}")
            print(f"The median of the data {data} is {adv_processor.calculate_median()}")
            print(f"The average after upgrading method is {adv_processor.safe_average()}")
        except (InvalidDataError, IndexError) as e:
            print("Failed", e)

    # 2. Test Text Cleaner
    for data in test_inputs:
        try:
            cleaner = TextCleaner(data)
            print(f"Cleaned: {cleaner.clean()}")
        except InvalidDataError as e:
            print("Failed", e)
    
    print("--- Done. Check app.log for details ---")

if __name__ == "__main__":
    main()