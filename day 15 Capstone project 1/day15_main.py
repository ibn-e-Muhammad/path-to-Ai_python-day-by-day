import logging
import os
from exceptions import InvalidDataError
from day15_data_collector import DataCollector


#logging
logging.basicConfig(
    filename = os.path.join(os.path.dirname(__file__), "app.log"),
    level=logging.DEBUG,
    format = "%(asctime)s, %(levelname)s, %(message)s",
    filemode="w"
)
#main orchestration

def main():
    # Test Data (Simulating inputs)
    # test_inputs = [
    # [1, 2, 3],
    # [],
    # [1, "a", 3],
    # [23, 45, 6, 2, 100, 1, 1000, 10],
    # "123",
    # ["123  !  ", "abc"],
    # [0, -1, 2, 3, -5, 8, -13, 21],
    # ["@ali", "  HiNa!!!", "  *baZooka##  "]
    # ]

    print("--- Starting Processing ---")

    data_collector = DataCollector()
    data_collector.collect_data()
    data_collector.data_entry()
    data_collector.display_stored_data()

    # 1. Test Number Processor and Database Input 
    # for data in test_inputs:
    #     print(f"\nProcessing input: {data}")
        
    #     # Try DataProcessor 1
    #     try:
    #         processor = DataProcessor(data)
    #         # print(f"DataProcessor Output: {processor.process()}")
    #         processor.process()
    #     except InvalidDataError as e:
    #         print(f"DataProcessor skipped: {e}")
            
        # Try TextCleaner 2
        # try:
        #     str_clean = TextCleaner(data)
        #     print(f"TextCleaner Output: {str_clean.process()}")
        # except InvalidDataError as e:
        #     print(f"TextCleaner skipped: {e}")
        

if __name__ == "__main__":
    main()