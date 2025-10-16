#AS computer science
#16/10/25
#Sum of Odd Numbers
#Reuben Joseph
#Greg Allcock



def main():
    total = 0
    total2 = 0
    my_array = [7, 5, 10, 8, 20] # Array with odd and even numbers
    for num in my_array:
        total += num

    print(f"The sum is {total}") #Prints sum of all numbers

    for num in my_array:
        if num % 2 != 0:
            total2 += num
    
    print(f"The sum of the odd numbers is {total2}") #Prints sum of ONLY odd numbers
        


main()

