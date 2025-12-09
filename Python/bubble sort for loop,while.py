#Reuben Joseph
#20/11/25
#Computer Science
#Greg Allcock
#Bubble sort


my_list = [23,41,11,17,34,56]

print(my_list)
n = len(my_list)-1
swapped = True

while swapped and n > 0:
    swapped = False
    for index in range(0,n):
        if (my_list[index] > my_list[index+1]):
            temp = my_list[index]
            my_list[index] = my_list[index+1]
            my_list[index+1] = temp

            swapped = True

    n = n -1
print(my_list)
print(f"The length of the list is {n}")






