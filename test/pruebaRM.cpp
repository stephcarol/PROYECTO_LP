#include <iostream>

#define PI 3.14

float add(float a, float b) {
    return a + b;
}

int main() {
    float x = 5.5;
    double y = 10.1;
    char c = 'A';
    int z = 3;
    const int CONSTANT = 10;
    static int static_var = 0;

    if (x < y) {
        z += static_cast<int>(x);
    } else {
        z -= static_cast<int>(y);
    }

    switch(z) {
        case 1:
            std::cout << "Case 1" << std::endl;
            break;
        case 2:
            std::cout << "Case 2" << std::endl;
            break;
        default:
            std::cout << "Default case" << std::endl;
            break;
    }

    for (int i = 0; i < 5; i++) {
        std::cout << "i: " << i << std::endl;
    }

    while (z > 0) {
        std::cout << "z: " << z << std::endl;
        z--;
    }

    do {
        std::cout << "Static variable: " << static_var << std::endl;
        static_var++;
    } while (static_var < 5);

    int* p = new int[10];
    for (int i = 0; i < 10; i++) {
        p[i] = i * 2;
    }
    delete[] p;

    try {
        throw "An error occurred";
    } catch (const char* msg) {
        std::cerr << msg << std::endl;
    }

    std::cout << "Size of int: " << sizeof(int) << std::endl;
    std::cout << "PI: " << PI << std::endl;

    return 0;
}
