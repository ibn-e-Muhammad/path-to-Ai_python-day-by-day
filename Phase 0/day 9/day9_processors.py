import logging

class DataProcessor:

    def __init__(self, data):
        """
        Constructor: This runs when you create the object.
        self.data is now a property of the object.
        """
        self.data = data
        logging.info(f"DataProcessor initialized with {len(data)} items.")



    def count_positive(self):
        """
        Refactor your old function here.
        Rule: Return 0 if list is empty, not None.
        Rule: Log the result before returning.
        """
        # TODO: Implement logic to count positive numbers in self.data
        count = 0
        nums = self.data
        if not nums:
            logging.info("The data list is empty")
            return 0
        else:
            for num in nums:
                if num > 0:
                    count += 1
        logging.info(f"The total positive numbers are {count}")
        return count



    def safe_average(self):
        """
        Refactor your old function here.
        Rule: Handle ZeroDivisionError using try/except.
        Rule: Log an error if the list is empty/sum fails.
        """
        # TODO: Implement logic to average self.data
        nums = self.data
        if not nums:
            logging.info("The data list is empty")
            return None
        else:
            try:
                return sum(nums)/len(nums)
            except ZeroDivisionError:
                logging.error("The division failed due to zero divisor error")