import logging
import os
from exceptions import InvalidDataError
from day16_data_collector import DataCollector


#logging
logging.basicConfig(
    filename = os.path.join(os.path.dirname(__file__), "app.log"),
    level=logging.DEBUG,
    format = "%(asctime)s, %(levelname)s, %(message)s",
    filemode="w"
)
#main orchestration

def main():

    print("--- Starting Processing ---")

    data_collector = DataCollector()
    data_collector.collect_data()
    data_collector.data_entry()
    data_collector.display_stored_data()

if __name__ == "__main__":
    main()