#include <iostream>
using namespace std;
void updateValue(int& ref, int* ptr) {
	ref = 20;
	*ptr = 30;
}
int main() {
	int a = 10;
	int b = 15;
	int* p = &b;
	updateValue(a, p);
	switch (a) {
	case 20:
		cout << "a es 20" << endl;
		break;
	default:
		cout << "a no es 20" << endl;
	}
	cout << "b es " << b << endl;
	return 0;
}
