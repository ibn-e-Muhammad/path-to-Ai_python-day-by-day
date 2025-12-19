def safe_average(nums):
    if not nums:
        return None
    else:
        return sum(nums)/len(nums)
    
def clean_words(words):
    cleaned_lst = []
    for word in words:
        word = word.lower()
        word = word.strip()
        word = word.strip("!@#$%")
        word = word.capitalize()
        cleaned_lst.append(word)
    return cleaned_lst


def count_positive(nums):
    count = 0
    if not nums:
        return None
    else:
        for num in nums:
            if num > 0:
                count += 1
    return count





