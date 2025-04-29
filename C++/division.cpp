#include <iostream>
using namespace std;
int main() {
    float a, b;
    cout << "Escribe los numeros para dividir: ";
    cin >> a >> b;
    if (b != 0)
        cout << "resultado: " << a / b << endl;
    else
        cout << "No se puede dividir entre cero." << endl;
    return 0;
}
