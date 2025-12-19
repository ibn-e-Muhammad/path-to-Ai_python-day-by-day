import logging
from exceptions import InvalidDataError
from day13_processors import DataProcessor


testval = [0, -1, 2, 3, -5, 8, -13, 21]
def main():
    test = DataProcessor(testval)
    print(test.process())

if __name__ == "__main__":
    main()