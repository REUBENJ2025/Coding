#Template
#As Computer Science
#Employee User Login
#16/10/25
#Reuben Joseph
#Greg Allcock

first_name = (input("Enter first name: "))
last_name = (input("Enter last name: "))

username = last_name + first_name[0] + "1"

print(username)

file = open("EmployeeLogin.txt")