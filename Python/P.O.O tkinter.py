import tkinter as tk
from tkinter import messagebox
class SumaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma")
        tk.Label(root, text="Primer número:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Segundo número:").grid(row=1, column=0, padx=10, pady=5)
        self.entry1 = tk.Entry(root)
        self.entry2 = tk.Entry(root)
        self.entry1.grid(row=0, column=1, padx=10, pady=5)
        self.entry2.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(root, text="Sumar", command=self.calcular).grid(row=2, column=0, columnspan=2, pady=10)
        self.resultado = tk.Label(root, text="")
        self.resultado.grid(row=3, column=0, columnspan=2)
    def calcular(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            suma = a + b
            self.resultado.config(text=f"Resultado: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos.")
root = tk.Tk()
app = SumaApp(root)
root.mainloop()
