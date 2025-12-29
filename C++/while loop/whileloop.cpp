#include <iostream>
using namespace std;

int check(){
       int x;

    x = 1; 

    while(x <= 10000) {
        cout << x << "\n";
        x++;
        system("Pause");
    }
    return 0;
}

int main() {
   string choice;
   cout << "Run the program (y/n)? ";
   cin >> choice;
   if (choice == "y" ){
    check();
    return 0;
   }
   else{
    return 0;
   }
}





