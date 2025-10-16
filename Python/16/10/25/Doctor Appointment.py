#Template
#surgery table
#Reuben Joseph
#16/10/25
#AS Computer Science
#Greg Allcock



my_Array = [
    [1, "9:00", "5877RC"],
    [2, "9:30", "9655AS"],
    [3, "10:00", ""],
    [4, "10:30", "8754TT"],
    [5, "11:00", ""],
    [6, "11:30", "8745SD"],
    [7, "13:00", "9635GH"],
    [8, "13:30", ""],
    [9, "14:00", "9874PL"],
    [10, "14:30", "9658SV"]
]

global user_appointment
user_appointment = input("Please enter your customerID: ").strip()

def findFirst():
    for i in range(len(my_Array)):
        if my_Array[i][2] == "":
            print(f"The first available appointment is at {my_Array[i][1]}")
            return "found"

    print("There are no available appointments today")
    return -1


findFirst()


