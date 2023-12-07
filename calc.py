import tkinter as tk
from tkinter import ttk

def calcular(operacion):
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set("Error")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("320x320")
ventana.configure(bg="#F0F0F0")

entrada = tk.Entry(ventana, font=("Arial", 20), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, font=("Arial", 20), bg="#F0F0F0").grid(row=1, column=0, columnspan=4, padx=10, pady=10)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 2
col_val = 0
for boton in botones:
    ttk.Button(ventana, text=boton, width=5, command=lambda boton=boton: entrada.insert(tk.END, boton)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ttk.Button(ventana, text='Calcular', width=20, command=lambda: calcular(entrada.get())).grid(row=row_val, column=0, columnspan=4, padx=10, pady=10)

ventana.mainloop()
