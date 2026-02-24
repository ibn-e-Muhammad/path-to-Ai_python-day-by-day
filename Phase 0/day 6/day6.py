students = [
    {"name": "Arslan", "scores": [82, 75, 91]},
    {"name": "Ali", "scores": [51, 60]},
    {"name": "Hina", "scores": [94, 89, 96, 99]},
    {"name": "Zara", "scores": []},
]

def student_averages(data):
    avg_score = {}
    for item in data:
        try:
            avg = sum(item["scores"])/len(item["scores"])
            avg_score[item["name"]] = avg
            print(avg)
        except ZeroDivisionError:
            avg = None
            avg_score[item["name"]] = avg
    return avg_score

print(student_averages(students))


words = [
    "cat","cat", "Apple", "Apple", "dog", "CAT", "orange",
    "apple", "Orange", "ORANGE", "cat",
]

def most_frequent(words):
    frq_word = ""
    clean_lst = []
    counter_lst = []
    count_num_lst = [1] * len(words)
    for word in words:
        clean_lst.append(word.lower())
    for word in clean_lst:
        if word in counter_lst:
            index = counter_lst.index(word)
            counter_val = count_num_lst[index]
            count_num_lst[index] = counter_val + 1
        else:
            counter_lst.append(word)
    frq_word = counter_lst[count_num_lst.index(max(count_num_lst))]    

    
    return frq_word

print(most_frequent(words))

# A less painfull way of doing it(not much painless though):

def most_frequent2(words):
    frq_word = ""
    counter_dict = {}
    counter = 0
    for word in words:
        for i in range(len(words)):
            if word.lower() == words[i].lower():
                counter += 1
                counter_dict[word.lower()] = counter
        counter = 0
    big = max(counter_dict.values())
    for key, value in counter_dict.items():
        if value == big:
            return key
print(most_frequent2(words))


data = [1, [2, [3, 4], 5], 6, [[7], 8], 9]

def deep_flatten(lst):
    flat_lst = []
    for x in lst:
        if type(x) == list:
            flat_lst.extend(deep_flatten(x))
        else:
            flat_lst.append(x)
        
    return flat_lst

print(deep_flatten(data))


nums = [10, 20, 20, 40, 50, 50, 60, 60, 60, 5]
#def second_largest_unique(nums):
#    lar = max(nums)
#    sec_unq = 0
#    for num in nums:
#        if max(nums) >= num:
#            sec_unq = num
    # my brain fried here.
# the below is done by the Ai
def second_largest_unique(nums):
    lar = max(nums)
    nums = list(set(nums))
    nums.remove(lar)
    sec_unq = max(nums)
    return sec_unq
# though this doesn't give the originally second largest that was unique in the orignal input. I don't know how do it. bye!
# moving on...

raw = ["@Arslan!!", "  *Hina ", "Danish##", " ZARA%%%  "]
def clean_names(raw):
    clean = []
    for w in raw:
        clean.append(w.lower().strip(" * !@#%").capitalize())
    return clean

# after that i checked with ai and it suggested:
def clean_names2(raw):
    clean = []
    return [clean.append(w.lower().strip(" * !@#%").capitalize()) for w in raw] #Absolutely Absurd

print(clean_names(raw))
print(clean_names2(raw))

#finally, the last one... yay(with meh expression)

text = """
Arslan is learning Python. Python is fun.
Robotics is the dream.
"""
def char_freq(text):
    # return dict of each character count (case-insensitive)
    # ignore spaces and newlines
    
    #return [ch_lst.append(w.lower().strip(" \n ") for w in text)]
    ch_lst = []
    counter = 0
    counter_dict = {}
    for ch in text:
        ch_lst.append(ch.lower().strip(" \n "))
    for i in range(len(ch_lst)):
        for ch in ch_lst:
            if ch == ch_lst[i] and ch != "":
                counter += 1
                counter_dict[ch_lst[i]] = counter
        counter = 0
    return counter_dict
    
print(char_freq(text))


            


