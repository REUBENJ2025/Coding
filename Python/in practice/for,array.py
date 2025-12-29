items = []

for i in range(5):
    user_input = input("Enter a number to add to the array: ")
    items.append(int(user_input))

for i in range(len(items)):
    print(f"Number {i + 1} is {items[i]}")
