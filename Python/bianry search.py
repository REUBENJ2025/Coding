#Greg Allcock
#05/11/25
#Binary Search
#Computer Science
#Reuben Joseph

wlist = [2,5,6,7,8,9,10] #List in order, 0:

found = False

search_term = int(input("Enter a search term: "))

#First and last pointed
first = 0
last = len(wlist) - 1

while (found == False and last >= first):
    mid = (first+last)//2 #Floor division, finds middle value in list
    if search_term == wlist[mid]:
        found = True
        break
    else:
        if (search_term > wlist[mid]):
            first = mid + 1
        elif (search_term < wlist[mid]):
            last = mid - 1

if (found == True):
    print("Found data Item")
else:
    print("Data Item not found")

