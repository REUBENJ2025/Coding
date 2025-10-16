#ReubenJoseph
#Greg Allock
#02/10/25
#AS Computer Science
#Counting Odd or Even

# Defined List for odd or even checking

list = {23, 54, 60, 12, 11, 15, 22}

for number in list:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")