from day8_utils import clean_words, count_positive, safe_average
from day8_data import lst, str_lst
def main():
    print(clean_words(str_lst))
    print(count_positive(lst), "positive numbers in the list.")
    print(safe_average(lst), "is the average score.")


if __name__ == "__main__":
    main()