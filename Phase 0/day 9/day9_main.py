import logging
# We import our classes from the other files
from day9_processors import DataProcessor
from day9_cleaners import TextCleaner

# 1. SETUP LOGGING
# This configures logging for the ENTIRE application
logging.basicConfig(
    filename="app.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='w', # Overwrites log file each run (good for testing)
    #force = True #(to force the python to log the thigns)
)

def main():
    # Test Data (Simulating inputs)
    numbers = [0, -1, 2, 3, -5, 8, -13, 21]
    dirty_words = ["@ali", "  HiNa!!!", "  *baZooka##  "]

    print("--- Starting Processing ---")

    # 1. Test Number Processor
    processor = DataProcessor(numbers)
    # Note: We are printing to console for user, but the Class logs internally too!
    print(f"Positives: {processor.count_positive()}")
    print(f"Average: {processor.safe_average()}")
    print(f"The Min value: {processor.get_extreme_values()[1]}")
    print(f"The Min value: {processor.get_extreme_values()[0]}")

    # 2. Test Text Cleaner
    cleaner = TextCleaner(dirty_words)
    print(f"Cleaned: {cleaner.clean()}")
    
    print("--- Done. Check app.log for details ---")

if __name__ == "__main__":
    main()