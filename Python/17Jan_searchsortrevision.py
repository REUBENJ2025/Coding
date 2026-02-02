#Binary Search

items = [10,20,30,40,50,60] #Items in order from smallest to largest 

first = 0 #Set size of items

last = len(items) - 1  #Set size of items

target = 40 #Item to search for

found = False #Conditional

while (found == False and first <= last): #Check if items in list or item has been found already
    mid = (first + last) //2 #Find mid value 

    if (items[mid] == target): #Checks to see if mid value is equal to target
        found = True
        break
    else:
        if (items[mid] > target): #Checks to see if middle value is greater than target and then removes items after mid
            last = mid - 1
        if (items[mid] < target): #Removes items lower than middle value and including 
            first = mid + 1

if found:
    print(f"{target} found")

#Insertion sort

items = [5,100,20,10,50,65]

for index in range(1,len(items)):
    current = items[index]
    index2 = index
    while(index2 > 0 and items[index2-1] > current):
        items[index2] = items[index2 -1]
        index2 = index2 - 1
        items[index2] = current

print(items)


#Bubble sort

items = [10,5,100,25,2,65]

n = len(items) - 1

swapped = True

while (swapped):
    swapped = False
    for index in range(n):
        while(items[index] > items[index + 1]):
            temp = items[index]
            items[index] = items[index + 1]
            items[index + 1] = temp
            swapped = True

n = n + 1

print(items)

    