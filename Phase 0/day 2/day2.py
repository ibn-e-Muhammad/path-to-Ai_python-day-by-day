    
nums = [1, 2, 3, 4, 5, 6, 7, 21, 8, 9, 10, 11, 12, 19, 20]


def find_max(n):
    largest = n[0]
    for i in n:
        if i > largest:
            largest = i
    
    return largest

print(find_max(nums))


def count_odds(n):
    odds = 0
    for i in n:
        if i % 2 != 0:
            odds += 1
    return odds

print(count_odds(nums))

name = "Arslan"
def reverse_str(n):
    rvs = ""
    for ch in n:
        rvs = ch + rvs
    return rvs

print(reverse_str(name))

def fizzbuzz():
    fizzbuzz_list = []
    for i in range(51):
        if i % 3 == 0:
            fizzbuzz_list.append("fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("buzz")
        else:
            fizzbuzz_list.append(i)

    print(fizzbuzz_list)
    
fizzbuzz()


def sum_of_evens(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
        else:
            pass
    return total

print(sum_of_evens([1,2,3,4,5,6,7,8, 51, 22]))



string_list = ["apple", "dog", "umbrella", "cat", "orange", "bat", "uukkk"]

def vowel_str(s):
    vowel_list = []
    for n in s:
        if n[0] in "aeiou":
            vowel_list.append(n)
    return vowel_list

print(vowel_str(string_list))