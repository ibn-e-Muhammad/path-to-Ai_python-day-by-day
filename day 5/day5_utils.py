def add(x, y):
    return x + y

def remove_spaces(s):
    return s.strip().replace(" ", "")

def average(nums):
    return sum(nums) / len(nums)

def safe_divide(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        print("Cannot Divide  By Zero, Try Again Please!")

def safe_convert(val):
    try:
        new_val = int(val)
    except ValueError:
        print("Failed to convert to Integer, please try again, or check the code logic!")

def introduce(user):
    print(f"My Name is {user['name']}, I am {user['age']}, and I know {", ".join(user['skills'])}.")


def clean_names(raw):
    clean_list = []
    for item in raw:
        clean_list.append(item.strip().replace(" ", "").lower().capitalize())
    
    return clean_list
    
