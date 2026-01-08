#Binary search

items = [10,20,30,40,50,60]

target = 20

found = False

first = 0

last = len(items) - 1

while (found == False and first <= last):
    mid = (first + last) // 2
    if items[mid] == target:
        found = True
        break
    else:

        if (items[mid] < target):
            first = mid + 1
        
        elif (items[mid] > target):
            last = mid - 1

if (found):
    print("Found")
        

#Bubble sort 

items = [1,1,5,3,2,100,30]

n = len(items) - 1

swapped = True

while (swapped and n > 0):
    swapped = False

    for index in range(0,n):
        if items[index] > items[index + 1]:
            temp = items[index]
            items[index] = items[index + 1]
            items[index + 1] = temp
            swapped = True
print(items)

#Insertion sort

items = [10,20,2,3,1,5,4,100,34]

for index in range(1,len(items)):
    current = items[index]
    index2 = index
    while index2 > 0 and items[index2 - 1] > current:
        items[index2] = items[index2 - 1]
        index2 = index2 - 1
        items[index2] = current

print(items)