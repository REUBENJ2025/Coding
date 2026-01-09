import array


def my_num(x):
    return x + 1

result = my_num(5)
print(result)

def my_text(s):
    return s.upper()

text_resize = my_text("hello")

print(text_resize)

def my_array(arr = []):
    user_choice = int(input("Enter a number to add to the array: "))
    arr.append(user_choice)
    print(arr)
    return arr

array_result = my_array()

def remove_item(arr = []):
    if len(arr) == 0:
        print("Array is empty, cannot remove item.")
        return arr
    removed_item = arr.pop(0)
    print(f"Removed item: {removed_item}")
    return arr

print(array_result)

def clear_array(clear_choice):
    if clear_choice == 1:
        array_result.clear()

while True:
    choice = input("Remove Item (y/n)? ")
    if choice.lower() == "y":
        update_array = remove_item(array_result)
        print(update_array)
    elif choice.lower() == "n":
        choice2 = input("Add Item (y/n)? ")
        if choice2.lower() == "y":
            array_result = my_array(array_result)

