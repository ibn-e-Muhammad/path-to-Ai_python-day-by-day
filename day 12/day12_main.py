import logging
import os
from day12_processors import DataProcessor
from day12_db import DatabaseManager
from exceptions import InvalidDataError


# establish Logger
logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), "app.log"), 
    level = logging.DEBUG,
    format = "%(asctime)s, %(levelname)s,%(message)s",
    filemode = 'w'
)

# orchestrating logic
def main():
    # Test Data (Simulating inputs)
    test_inputs = [
    [1, 2, 3],
    [],
    [1, "a", 3],
    [23, 45, 6, 2, 100, 1],
    "123",
    ["123  !  ", "abc"],
    [0, -1, 2, 3, -5, 8, -13, 21],
    ["@ali", "  HiNa!!!", "  *baZooka##  "]
    ]

    print("--- Starting Processing ---")

    # 1. Test Number Processor and Database Input
    db = DatabaseManager()
    for data in test_inputs:
        try:
            #creating objects
            processor = DataProcessor(data)
            avg = processor.safe_average()
            if avg is not None:
                db.save_result("Average: ", avg)
            results = db.fetch_all_results()
            for row in results:
                print(row)
            
        except (InvalidDataError, IndexError) as e:
            print("Failed", e)
            logging.error(f"Processing failed for data {data}: {e}")
  # for testing only ==>      db.delete_all_results()
    db.close()


if __name__ == "__main__":
    main()  