arr = [10,20,30,40,50,60,70,80,90,100, 6, 1, 5, 2, 8, 0, 11, 3]

words = ["apple","cat","apple"," dog ","cat","apple","  apple","Umbrella","orange","Egg","Blue","cake","Cat"]


def multi_func(arr):
    min_val = min(arr)
    max_val = max(arr)
    sum_val = sum(arr)
    return min_val, max_val, sum_val

print(multi_func(arr))

def clean_str(words):
    str_clean_list = []
    for word in words:
        str_clean_list.append(word.lower().strip())
    return str_clean_list

print(clean_str(words))


def list_tuple(words):
    tuple_list = []
    word_len = 0
    for word in words:
        word_len = len(word)
        tuple_list.append((word, word_len))
        word_len = 0
    return tuple_list

print(list_tuple(words))

# Another way to do the above problem:
tuple_list = [(w, len(w)) for w in words]
print(tuple_list)


keys = ["name", "age", "dream"]
values = ["Arslan", 20, "Robotics"]



def list_merger(keys, values):
    mer_dict = {}
    ## wrong logic:
    # mer_dict[[key for key in keys]] = [value for value in values]
    i = 0
    for key in keys:
        mer_dict[key] = values[i]
        i += 1
    return mer_dict

print(list_merger(keys, values))


def filt_func(nums):
    filt_list = []
    for num in nums:
        if num % 2 != 0:
            filt_list.append(num*num)
    return filt_list

print(filt_func(arr))


students = [
    ("Arslan", 82),
    ("Ali", 51),
    ("Hina", 94),
    ("Zara", 67),
    ("Danish", 33)
]

def categorize(students):
    cat_dict = {
        "pass":[],
        "fail": [] 
    }
    for student in students:
        if student[1] >= 60:
            cat_dict["pass"].append(student[0])
        elif student[1] < 60:
            cat_dict["fail"].append(student[0])
        else:
            print("Error, bad luck")
        

    return cat_dict

print(categorize(students))

