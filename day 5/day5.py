arr = [[1,2,3], [4,5], [6,7,8,9,10]]

def flatten(arr):
    sublist = []
    for item in arr:
        for sub_item in item:
            sublist.append(sub_item)
    return sublist

print(flatten(arr))
# Another way:
sub_list = [item for sublist in arr for item in sublist] # done with the help of Ai
print(sub_list)

def count_evens(arr):
    count = 0
    for sublist in arr:
        for item in sublist:
            if item % 2 == 0:
                count += 1
    return count

print(count_evens(arr))

people = [
    {"name": "Arslan", "age": 20},
    {"name": "Hina", "age": 19},
    {"name": "Zara", "age": 22}
]

def names_only(people):
    name_list = []
    for key in people:
        name_list.append(key["name"])
    return name_list

print(names_only(people))

scores = {"Arslan": 82, "Ali": 51, "Hina": 94, "Zara": 67}

def top_scorers(scores):
    top_score_list = []
    for key in scores:
        if scores[key] >= 70:
            top_score_list.append(key)
    return top_score_list
print(top_scorers(scores))





