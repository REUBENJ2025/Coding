#Greg Allcock
#04/11/25
#Linear search
#Computer Science
#Reuben Joseph

#Create a list of terms
nlist = [12,4,5,6,7,8,2,2,34,54545,664,332,55,1112,3433,22212,444,2322,33,211,344]

#Take user input
user_search = int(input('Enter a number: '))

#Sets found to false
Found = False



for i in range(len(nlist)): #Looks through the range of the list until data is found
    if (user_search == nlist[i]):
        Found = True #Sets found to true if found data item
        
if (Found == True): #If the data item is found print data item found
        print(f"Found data item {user_search}")

else: #Prints not found if data item does not exist
    print("Data Item not found")
