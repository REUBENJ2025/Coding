#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> numbers = {23, 54, 11, 22, 55, 67, 78};  // List of numbers to check
    for (int num: numbers) {
        if (num % 2 == 0) {
            cout << num << " is even" << endl;
            system("pause");
        } else {
            cout << num << " is odd" << endl;
            system("pause");
        }
    }
}
