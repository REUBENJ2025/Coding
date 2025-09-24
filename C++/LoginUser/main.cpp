#include <iostream> //Library import for the input output streams including the cout and cin methods
#include <vector> //Library import for the vector method


using namespace std;  //Declare the namespace std prevents us having to prefic cout and cin statments with the std:: scope resolution operator 

//Define the vectors globally
vector<string> usernames = {"Bob", "Mike", "Jim"}; 
vector<int> passwords = {1111, 1234, 0000};

//Define the SignUp function
int signup () {
    
    

    string user_username;
    cout << "Please enter a username";
    cin >> user_username;

    int user_password;
    cout << "Please enter a password:";
    cin >> user_password;

    passwords.push_back(user_password);
    

    usernames.push_back(user_username); //Take the entered username and add to the end of the vector using the push_back method

    cout << "***********************" << endl << endl;
    cout << "*****New User List*****"<< endl << endl;

    for (const auto& element : usernames) {   //For loop that automatically assigns a data type and then iterates through each element of the usernames vector
    cout << "\t" << element << endl << endl;  //output each element to the screen with two end line commands for two carriage returns
    }


   
    system("Pause"); //Add a system pause so the console window does not automatically closes
    return 0; //return 0 exits the function

}


int main()
{   int choice;   //Choice menu for signup or login options
    cout << "Please press 1 for Signup or press 2 for login: ";
    cin >> choice;

    if (choice == 1){
         cout << "User SignUp" << endl << endl;
        signup(); //For signup call the signup function and then once the sign function is complete it returns 0 to terminate the function and returns control to this main function where we then terminate the main funciton
        return 0;
    }

    cout << "User Login" << endl << endl; //Else option 2 executes the below code

    string user_username;    //Request and input username
    cout << "Please enter your username";
    cin >> user_username;

    int user_password;     //Request and input password
    cout << "Please enter your password:";
    cin >> user_password;

    for (unsigned int i = 0; i<passwords.size(); i++)  //For loop uses unsigned int i as iterator as vectors can only be poisitve integers, until end of vector is reached, each loop increments value of i by 1 i++
    {
        if (user_password == passwords[i] && user_username == usernames[i]) //If the value of user_password entered by the user equals the password stored in the current element of the passwords vector and the same for 
                                                                            //user_username execute
        {
            cout << "Login Successful";
            system("Pause");
            return 0;                //Exit function
        }
    
        
    }
    //else cout below text
    cout << "Invalid Password or Username" << endl << endl;
   

    system("Pause");  //Pause the terminal window until a key is pressed
}