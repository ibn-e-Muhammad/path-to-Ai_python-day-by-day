import logging
import os
from exceptions import InvalidDataError
from day19_file_processor import FileProcessor


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

    FileProcessor()


if __name__ == "__main__":
    main()