'''even = 0
odd = 0

for i in range(10):
    user_input = int(input("Enter a number: "))
    if user_input % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1



print(f"There was {odd} odd numbers(s) and there was {even} even number(s)")
'''
'''
total = 0
scores = []

for i in range(6):
    user_input = int(input("Enter a score: "))
    scores.append(user_input)

for i in range(len(scores)):
    total = total + scores[i]

average = total / len(scores)

largest = max(scores)

lowest = min(scores)

print(f"The largest score was {largest}, the lowest score was {lowest} and the average score was {average}")
'''
'''
numbers = []

for i in range(8):
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)

for i in range(len(numbers)):
    index = numbers[i]
    index2 = numbers[i - 1]
    if(index > index2):
        largest_second_num = index
        smallest_num = index2
    elif(index2 > index):
        largest_second_num = index2
        smallest_num = index
    elif(index == index2 or index2 == index):
        print("Both numbers are the same")

print(f"The largest second number is {largest_second_num} and the smallest second number is {smallest_num}")
'''



def prime(nums):
    prime = 0
    not_prime = 0 
    for i in range(len(nums)):
        user_input = nums[i]
        if user_input > 1:
            for j in range(2, user_input):
                if (user_input % j) == 0:
                    not_prime += 1
                    break
            else:
                prime += 1
    return prime, not_prime

nums = []

for i in range(10):
    user_input = int(input("Enter a number: "))
    nums.append(user_input)

prime, not_prime = prime(nums)
print(f"There were {prime} prime numbers and {not_prime} non-prime numbers.")

prime(nums)