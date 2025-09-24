#Computer Science
#Gregg
#Python Login program
#20/09/25

#Define Username and Password arrays
array_database = ["John", "Mike", "Jim"] 
array_database2 = ["1234", "1111", "password"]

#Login Function
def login():
    username = input("Username: ")
    password = input("Password: ")

    # Loop through all usernames and passwords
    for i in range(len(array_database)): # i is each element of the array until the end
        if username == array_database[i] and password == array_database2[i]: #If statement checks to see if the current element in the username array and the password entered exists in the password array.
            print("Login successful!")
            return # Stop the function as login is successful
    # If loop finishes without finding a match
    print("Invalid username or password.")

def signup(): #Signup Procedure
    username = input("Username: ")
    password = input("Password: ")

    array_database.append(username) #Adds username input the username array
    array_database2.append(password) #Adds password input to the password array

    print(array_database, array_database2)

choice = int(input("Press 1 to login or Press 2 to register"))

if choice == 1: #Checks whethere user wants to Login or Signup
    print("Login selected")
    login()
elif choice == 2:
    print("Signup selected")
    signup()
else:
    print("No correct option selected")