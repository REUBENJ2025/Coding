#Binary Search

items = [10,20,30,40,50,60] #Create a list of numbers in order assigned to items. Must be in order (Ascending or Descending)

first = 0 #Assigning the variable first to 0 to indicate the first position of items is 0

last = len(items) -1 #Assign last to length of items - 1 to get length of items to be 0-5

found = False #Assing found to false to be used as a conditional statement once item is found

target = 30 #Random target to find through binary search

while (found == False and first <= last): #While loop to check if item is not found and there are items in the list and then finds middle value in items
    mid = (first + last) //2
    if (items[mid] == target): #Checks through each iteration of the while loop and new mid point if mid is equal to target value and then stop the program
        found = True
        break
    else:
        if (items[mid] < target): #Checks to see if the middle value is less than target value and discards previous items before the mid value
            first = mid + 1
        elif (items[mid] > target): #Checks to see if items[mid] is greater than target and if is then any values higher than mid are discarded
            last = mid - 1

if (found):
    print(f"{target} was found at postion {items[mid]}")
else:
    print(f"{target} was not found")


#Linear Search

items = [30,10,5,7,2,1] #Create a list of items

target = 7 #Set a value to look for 

found = False #Set a condition

for i in range(len(items)): #Iterate through the length of the list until item is found or not found
    if items[i] == target:
        found = True

if (found): #Print the outcome
    print(f"{target} was found")
else:
    print(f"{target} was not found")

#Bubble Sort

items = [10,5,100,25,15,10] #Create list of items

n = len(items) - 1 #Set n as the length of items 0,length

swapped = True #Set swapped to true in order for while loop to start

while (swapped): #Check to see if an item has been swapped
    swapped = False

    for index in range(n): #For loop to iterate through items
        if (items[index] > items[index + 1]): #Checks if first value is greater than consecutive item
            temp = items[index] #Set temp to first value
            items[index] = items[index + 1] #Swap values
            items[index+ 1] = temp #Set temp to next item
            swapped = True 
n = n + 1 #Indent outside of while and for

print(items)


#Insertion Sort

items = [100,50,30,200,500,350] #List of items

for index in range(1,len(items)): # For loop starting from 1 for sorted and unsorted list
    current = items[index] #Set current value to unsorted item
    index2 = index #Create sorted list
    while(index2 > 0 and items[index2 - 1] > current): #Index2 > 0 checks there is items to be sorted and if previous item is greater than current
        items[index2] = items[index2 - 1] # Move to sorted list
        index2 = index2 - 1 #move back through list
        items[index2] = current #new vslue

print(items)


#Queue
arr = []
head_pointer = -1
rear_pointer = 0
MAX_SIZE = 10



def array(user_val,):
    arr.append(user_val)
    print(arr)
    return



def dequeue():
    arr.pop(0)
    return 



def enqueue():
    user_val = int(input("Enter a value to enqueue: "))
    update_arr = array(user_val)
    return 



while True:
    
    print("-----------------------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    


    user_input = int(input("Enter a number 1-3: "))

    if user_input == 1 and len(arr) <= MAX_SIZE - 1:
        new_enqueue = enqueue()
        head_pointer = 0
        rear_pointer += 1
        print(f"Head pointer is at position {head_pointer} and rear pointer is at position {rear_pointer}")
    if user_input == 1 and len(arr) > MAX_SIZE:
        print("Overflow error, queue is full")

    elif user_input == 2 and head_pointer > -1:
        new_dequeue = dequeue()
        head_pointer += 1
        print(arr)
        print(f"The head pointer is at position {head_pointer} and rear pointer is at position {rear_pointer}")
    elif user_input == 2 and head_pointer == -1:
        print("Underflow error, queue is empty")
    elif user_input == 3:
        try:
            print(arr[-1])
        except:
            print("There are no items to peek")
