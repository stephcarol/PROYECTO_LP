#include <iostream>

#define PI 3.14
using namespace std;
float add(float a, float b) {
    return a + b;
}

 void updateValue(int &ref, int *ptr)
    {
        ref = 20;
        *ptr = 30;
    }

int main() {
    //Rafael Merchan
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
    //Rafael Merchan 


    //Stephany Cabezas
    // Declaración de variables
    int a = 0;

    // Bucle for
    for(a = 0; a < 10; a++) {
        std::cout << "Hola mundo" << std::endl;
    }

    // Comentario de una línea

    // Comentario de bloque
    /*
    Esto es otro comentario
    */

    // Entrada de usuario
    std::cin.get();

    // Retorno de valor
    return 0;
    //Stephany Cabezas

    //Sebasceb

   
   
        int a = 10;
        int b = 15;
        int *p = &b;
        updateValue(a, p);
        switch (a)
        {
        case 20:
            cout << "a es 20" << endl;
            break;
        default:
            cout << "a no es 20" << endl;
        }
        cout << "b es " << b << endl;
        return 0;
    
}
