#Linear search




items = [10,30,1,50,25]

term = 1000

found = False

for i in range(len(items)):
    if items[i] == term:
        found = True

if (found):
    print(f"{term} found!")
else:
    print("Not Found")

#Bubble sort

items = [20,30,10,100,25,1]
n = len(items) - 1

swapped = True

while(swapped == True and n > 0):
    swapped = False
    for index in range(0,n):
        if items[index] > items[index + 1]:
            temp = items[index]
            items[index] = items[index + 1]
            items[index + 1] = temp
            swapped = True

print(items)

#insertion sort

items = [10,100,30,5,1,2,3]

for index in range(1,len(items)):
    current = items[index]
    index2 = index
    while index2 > 0 and items[index2 -1] > current:
        items[index2] = items[index2 - 1]
        index2 = index2 - 1
        items[index2] = current

print(items)

#Linear search

items = [10,30,1,3,2,100,30,25]

target = 1

found = False

for i in range(len(items)):
    if (items[i] == target):
        found = True

if (found):
    print("Found")

#Binary search

items = [10,20,30,40,50,60]

target = 30

first = 0

found = False

last = len(items) - 1

while (found == False and last > first):
    mid = (first + last) //2
    if target == items[mid]:
        found = True
        break
    else:

        if target > items[mid]:
         first = mid + 1
        elif target < items[mid]:
            last = mid - 1

if (found == True):
    print("Found")