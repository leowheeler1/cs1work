#include <iostream>
using namespace std;

int main()
{
    int my_num; // Declaring a Variable
    // Ask user for input
    cout << "How many repeats do you want? ";
    cin >> my_num;
    // In a for loop, print message
    for (int i = 0; i < my_num; i++) { // I++ means I += 1
        cout << i << ": Kiss my ass!\n";
    }
    cout << "Exiting Now.\n";
    return 0;
}