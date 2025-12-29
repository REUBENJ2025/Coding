#Reuben Joseph
#20/11/25
#Computer Science
#Greg Allcock
#Bubble sort


my_list = [23,41,11,17,34,56]

n = len(my_list)-1
swapped = True

while(swapped):
    swapped = False

    for index in range(0,n):
        if(my_list[index] > my_list[index+1]):
            temp = my_list[index]
            my_list[index] = my_list[index+1]
            my_list[index+1] = temp

            swapped = True


print(my_list)




