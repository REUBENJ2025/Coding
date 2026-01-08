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
    return arr

array_result = my_array([10])

def remove_item(arr = []):
    if len(arr) == 0:
        print("Array is empty, cannot remove item.")
        return arr
    removed_item = arr.pop(0)
    print(f"Removed item: {removed_item}")
    return arr

print(array_result)

update_array = remove_item(array_result)
print(update_array)