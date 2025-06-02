import tkinter as tk
from tkinter import messagebox
class Suma:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calcular(self):
        return self.a + self.b
def realizar_suma():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        operacion = Suma(a, b)
        resultado = operacion.calcular()
        messagebox.showinfo("Resultado", f"El resultado es {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
def main():
    global entrada1, entrada2
    ventana = tk.Tk()
    ventana.title("Suma de dos números")
    tk.Label(ventana, text="Ingresa el primer número:").pack()
    entrada1 = tk.Entry(ventana)
    entrada1.pack()
    tk.Label(ventana, text="Ingresa el segundo número:").pack()
    entrada2 = tk.Entry(ventana)
    entrada2.pack()
    boton = tk.Button(ventana, text="Calcular suma", command=realizar_suma)
    boton.pack()
    ventana.mainloop()
if __name__ == "__main__":
    main()
