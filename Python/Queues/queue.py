

def menu(items, head_pointer, rear_pointer):

    while True:
        print("Queue Operations: \n")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Clear Queue")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            head_pointer, rear_pointer = enqueue(items, head_pointer, rear_pointer)
        elif choice == 2:
            head_pointer, rear_pointer = dequeue(items, head_pointer, rear_pointer)
        elif choice == 3:
            print(items)
        elif choice == 4:
            items.clear()
            head_pointer = 0
            rear_pointer = -1
            print("Queue cleared.")
        else:
            print("Exiting...")
            return

def enqueue(items, head_pointer, rear_pointer):
    user_input = input("Enter an item to add to the queue: ")
    items.append(user_input)
    rear_pointer += 1
    print(items)
    print(f"Head Pointer: {head_pointer}, Rear Pointer: {rear_pointer}")
    return head_pointer, rear_pointer
   
    

def dequeue(items, head_pointer, rear_pointer):
    if rear_pointer == -1:
        print("Queue is empty. Cannot dequeue.")
        print("Head Pointer:", head_pointer, "Rear Pointer", rear_pointer)
    else:
        removed = items.pop(0)
        head_pointer += 1
        rear_pointer -= 1
        print(f"Removed item: {removed}")
    print(f"Current queue: {items}")
    print(f"Head Pointer: {head_pointer}, Rear Pointer: {rear_pointer}")
    return head_pointer, rear_pointer


items = []
head_pointer = 0 
rear_pointer = -1
menu(items, head_pointer, rear_pointer)
