import logging
from exceptions import InvalidDataError

class BaseProcessor:
    def __init__(self, data):
        self._validate(data)
        self.data = data
        logging.info(f"{self.__class__.__name__} initialized.")

    def _validate(self, data):
        raise NotImplementedError("Validaction not implemented")


    def process(self):
        raise NotImplementedError("Process method not implemented from the base class.")
