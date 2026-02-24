import logging
from exceptions import InvalidDataError

class TextCleaner:
    def __init__(self, raw_words):
        if not isinstance(raw_words, list):
            logging.critical("Data is not a list")
            raise InvalidDataError("Data must be a list")
        for data in raw_words:
            if not isinstance(data, str):
                logging.error(f"Wrong data type of data {data}")
                raise InvalidDataError("Only strings can be entered.")
        self.raw_words = raw_words

    def clean(self):
        """
        Refactor your clean_words function here.
        Challenge: Can you do it in one line using a list comprehension?
        Hint: [w.lower().strip()... for w in self.raw_words]
        """
        # TODO: Implement logic to clean self.raw_words
        cleaned_lst = [w.lower().strip().strip("!@#$%*").capitalize() for w in self.raw_words]
        return cleaned_lst