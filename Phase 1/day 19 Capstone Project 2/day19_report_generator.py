import logging
from exceptions import InvalidDataError


class ReportGenerator():
    def __init__(self, df):
        self.df = df
        self.report_generator(self.df)


    def report_generator(self, df):
        try:
            # Process the DataFrame and generate a report
            # For demonstration, let's just print the summary statistics
            report = df.describe()
            print("Report Generated:")
            print(report)
        except Exception as e:
            logging.error(f"Error occurred while generating report: {e}")
        


    