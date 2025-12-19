name = "Arslan"
age = 20
print(f"Hi... I'm {name}, and I'm {age} years old but i feel like 80 inside. Though everyone knows I don't have wisdom of it.")

def square(n):
    return n*n

print(square(9))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 20]
for n in nums:
    print(n)


def even_giver(n):
    for i in n:
        if i%2 == 0:
            print(i)
        else:
            continue

even_giver(nums)

def even_giver2(n):
    result = []
    for i in n:
        if i%2 == 0:
            result.append(i)
    print(result)
    return result
    
even_giver2(nums)
