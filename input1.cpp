#include <iostream>
using namespace std;



int main() {
    int i = 0;

    while (i < 10) {
        if (i % 2 == 0) {
            i++;
        } else {
            i += 3;
        }
    }

    return 0;
}
