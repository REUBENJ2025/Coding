def binary_search():
    items = [10,20,30,40,50,60,70]

    first=0
    last = len(items) - 1
    target = 30
    found = False

    while(found == False and first > last):
        mid = (first + last)//2
        if mid == target:
            found = True
            break
        else:
            if (target > mid):
                first = mid +1

            elif (target < mid):
                last = mid - 1

    if (found):
        print(f"{target} is found")
    else:
        print(f"{target} was not found")

def bubble_sort():
    items = [20,1,5,2,0]
    n = len(items)-1
    swapped = True
    while(swapped):
        swapped = False
        for index in range(0,n):
            if items[index] > items[index + 1]:
                temp = items[index]
                items[index] = items[index + 1]
                items[index +1] = temp
            
                swapped = True
                
            

    print(items)

bubble_sort()

def linear_search():
    items = [10,20,40]

    target = 10

    found = False

    for i in range(len(items)):
        if items[i] == target:
            found = True
            
    if (found):
        print(f"Found {target}")

linear_search()
        
def insertion_sort():
    items = [10,2,3,100,50]
    swapped = False
    n = len(items) -1

    for index in range(1,n):
        current = index
        index2 = index
        if(items[index2 -1] > items[index]  and current > 0):
            items[index2] = items[index2 -1]
            items[index2] = current
            index2 = index2 + 1
            swapped = True

    print(items)
        
