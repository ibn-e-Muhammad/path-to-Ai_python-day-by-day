import logging
import pandas as pd
import numpy as np
from pathlib import Path
from day19_report_generator import ReportGenerator

class FileProcessor:
    def __init__(self):
        self.access_file()


    def access_file(self):
        try:
            folder = Path(__file__).parent/"incoming_data"
            for file in folder.glob("*.csv"):
                self.file_path = file
                df = pd.read_csv(self.file_path)
                ReportGenerator(df)

                logging.info(f"Accessed file: {self.file_path}")
            return df
        except Exception as e:
            logging.error(f"Error occurred while accessing file: {e}")
            raise Exception(f"File access failed: {e}")