import logging
from exceptions import InvalidDataError
from day13_base_processor import BaseProcessor

class TextCleaner(BaseProcessor):
    def _validate(self, data):
        if not isinstance(data, list):
            logging.critical("Data is not a list")
            raise InvalidDataError("Data must be a list")
        for item in data:
            if not isinstance(item, str):
                logging.error(f"Wrong data type of data {item}")
                raise InvalidDataError("Only strings can be entered.")
        self.data = data

    def process(self):
        """
        Refactor your clean_words function here.
        Challenge: Can you do it in one line using a list comprehension?
        Hint: [w.lower().strip()... for w in self.raw_words]
        """
        # TODO: Implement logic to clean self.data
        cleaned_lst = [w.lower().strip().strip("!@#$%*").capitalize() for w in self.data]
        return cleaned_lst