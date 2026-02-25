import logging
import os
from exceptions import InvalidDataError



#logging
logging.basicConfig(
    filename = os.path.join(os.path.dirname(__file__), "app.log"),
    level=logging.DEBUG,
    format = "%(asctime)s, %(levelname)s, %(message)s",
    filemode="w"
)



