arr = [10,20,30,40,50,60,70,80,90,100]
str_list = ["apple", "Umbrella", "orange", "Egg", "Blue", "cake"]
nums = [3, 10, -5, 8, 99, 7, 11, -1, 4]
print(arr)
print(arr[2:5])
print(arr[::-1]) # reverse
print(arr[::2]) # every second element
print(arr[2:10:3]) # every third element form 2nd index to 10th index
print(arr[1::4]) # every forth element form 1st index to the last index


person = {
    "name": "Arslan",
    "age": 20,
    "dream": "Robotics"
}

print(person.items())
print(person.keys())
print(person.values())
### Practice start Day 3

def middle(a):
    return a[1:-1]

print(middle(arr))
 

def squares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return nums
print(squares(arr))


def count_vowel_words(words):
    count = 0
    for word in words:
        lo_word = word.lower()
        if lo_word[0] in "aeiou":
            count += 1
    return count

print(count_vowel_words(str_list))


words = ["apple","cat","apple","dog","cat","apple","apple","Umbrella","orange","Egg","Blue","cake","Cat"]

def freq(words):
    count = 0
    counter_dict = {}
    for i in range(len(words)):
        for word in words:
            if word.lower() == words[i].lower():
                count += 1
        counter_dict[words[i].lower()] = count
        count = 0
    return counter_dict

print(freq(words))




def sec_lar(nums):
    lar = nums[0]
    seclar = 0
    for num in nums:
       if num < max(nums) and num > seclar:
           seclar = num
    return seclar

print(sec_lar(nums))


