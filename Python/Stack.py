my_stack = []
max_items = 5
head_pointer = -1 

rear_pointer  = 0

def push(user_val): #Pushes an item on top of stack
    if len(my_stack) < max_items:
        my_stack.append(user_val)
    else:
        print("Stack Overflow Error, cannot add more items.")

def pop(): #Removes top item due to philosophy of stack
    try:
        removed_val = my_stack.pop()
        print(f"Item removed {removed_val}")
    except:
        print("Underflow Error, no items in stack to remove.")


def peek():
    try:
        print(f"The top item in the stack is {my_stack[-1]}")
    except:
        print("There are no items to peek at in the stack, the stack is empty.")


while True:
    print ("-------------------")
    print("1. Push an item onto the stack")
    print("2. Pop an item from the stack")
    print("3. Peek at the top item of the stack")
    print("4. Clear the stack")
    print("5. View the stack")

    user_choice = int(input("Enter a choice (1-5)"))

    if user_choice == 1:
        push_item = int(input("Enter a value to push onto the stack: "))
        update_push = push(push_item)
        head_pointer = head_pointer + 1
    if user_choice == 2:
        pop()
        head_pointer = head_pointer - 1

    if user_choice == 3:
        peek()
    if user_choice == 4:
        print("The stack is cleared")
        my_stack.clear()
    if user_choice == 5:
        print(f"View of current stack {my_stack}") 
        
    
        

