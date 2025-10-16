#Template
#As Computer Science
#Employee User Login
#16/10/25
#Reuben Joseph
#Greg 


"""  ______ __  __ _____  _      ______     ________ ______   _____       _______       ____           _____ ______ 
 |  ____|  \/  |  __ \| |    / __ \ \   / /  ____|  ____| |  __ \   /\|__   __|/\   |  _ \   /\    / ____|  ____|
 | |__  | \  / | |__) | |   | |  | \ \_/ /| |__  | |__    | |  | | /  \  | |  /  \  | |_) | /  \  | (___ | |__   
 |  __| | |\/| |  ___/| |   | |  | |\   / |  __| |  __|   | |  | |/ /\ \ | | / /\ \ |  _ < / /\ \  \___ \|  __|  
 | |____| |  | | |    | |___| |__| | | |  | |____| |____  | |__| / ____ \| |/ ____ \| |_) / ____ \ ____) | |____ 
 |______|_|  |_|_|    |______\____/  |_|  |______|______| |_____/_/    \_\_/_/    \_\____/_/    \_\_____/|______|
  """                                                                                                               


#imported os to create folder + file                                                                                                           
import os




#####################################################################################################################
###CREATES FOLDER AND FILE IN YOUR DOCUMENTS FOLDER IF YOU NEED TO REMOVE SHOULD LOOK LIKE: Documents/EmployeeData###
#####################################################################################################################
global file_path

documents_folder = os.path.join(os.path.expanduser("~"), "Documents")       #Section creates folder an file using the os libary
folder_name = os.path.join(documents_folder, "EmployeeData") #Creates Folder
file_path = os.path.join(folder_name, "Employeedatabase.txt") #Creates File
os.makedirs(folder_name, exist_ok = True) 

if not os.path.exists(file_path): #Uses Logic Gate Not, so it will not overwrite file if exists 
    with open(file_path, "a") as file:  #Appends to the file 
        file.write("---Employee Logins--")
        file.write("\n")
        

#Checks to see if user is in database by looking inside the file and returning specific values
def existingUsers(): 
    num = 1
    first_name = str(input("Please enter your First Name: "))
    last_name = str(input("Please enter your Last Name: "))
    base_username = last_name[0].upper() + last_name[1:].lower() + first_name[0].upper() + str(num)

    with open(file_path, "r") as file: #Opens file for read
        file_contents = file.read()
        

        while base_username in file_contents: #Continously asks user to input login username until there is not a duplicate by incrimenting by 1
            num = num + 1
            first_name = str(input("Please enter your First Name: "))
            last_name = str(input("Please enter your Last Name: "))
            base_username = last_name[0].upper() + last_name[1:].lower() + first_name[0].upper() + str(num)
            
        
        with open(file_path, "a") as file: #Appends to file without overwriting the file as "w" would do
          if base_username not in file_contents:
            file.write("\n")
            file.write(base_username)
            print("Username is unique") # Adds username to the file if unique
            return True
          if base_username in file_contents:
             return False


                    
             

            


        



existingUsers()