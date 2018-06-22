from tkinter import *


def sumar():
    try:
        v1 = int(var1.get())
        v2 = int(var2.get())
        print(v1+v2)
    except ValueError:
        print("Valores inválidos")


def restar():
    try:
        v1 = int(var1.get())
        v2 = int(var2.get())
        print(v1-v2)
    except ValueError:
        print("Valores inválidos")


def multiplicar():
    try:
        v1 = int(var1.get())
        v2 = int(var2.get())
        print(v1*v2)
    except ValueError:
        print("Valores inválidos")


def dividir():
    try:
        v1 = int(var1.get())
        v2 = int(var2.get())
        print(v1/v2)
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    except ValueError:
        print("Valores inválidos")


root = Tk()
etiq1 = Label(root, text="Primer operando")
input1 = IntVar()
var1 = Entry(root)
etiq2 = Label(root, text="Segundo operando")
input2 = IntVar()
var2 = Entry(root)
b1 = Button(root, text="+", command=sumar)
b2 = Button(root, text="-", command=restar)
b3 = Button(root, text="x", command=multiplicar)
b4 = Button(root, text="/", command=dividir)
etiq1.pack()
var1.pack()
etiq2.pack()
var2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()
