class Suma:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calcular(self):
        return self.a + self.b
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
operacion = Suma(n1, n2)
print("El resultado es", operacion.calcular())
