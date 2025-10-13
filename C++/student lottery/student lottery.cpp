//Computer Science
//Student lottery
//Reuben Joseph
//13/10/25
//Greg Allcock

#include <iostream> //Used for input and output
using namespace std;
#include <random> //Used for random number generation
#include <sstream> //Used to output a string one character at a time

int main(){
    cout << "Student lottery" << endl << endl;
    bool pause = false;
    while (pause == false){
    random_device rd;
    mt19937 gen(rd());
    discrete_distribution<> d({70, 20, 10}); // Probabilities for Lukas, Reuben, Pavel
    string choices[] = {"Lukas", "Reuben", "Pavel"};
    cout << choices[d(gen)] << endl << endl;
    string choice;
    cout << "Would you like to run the lottery again? (y/n): ";
    cin >> choice;
    if (choice == "n"){
        pause = true;
    }
    else if (choice == "y")
    {
        pause = false;
    }
    
    
    }

}