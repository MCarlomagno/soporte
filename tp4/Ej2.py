from tkinter import *


def escribir0():
    aux = entrada.get()
    aux = aux + "0"
    entrada.set(aux)
    return entrada

def escribir1():
    aux = entrada.get()
    aux = aux + "1"
    entrada.set(aux)
    return entrada

def escribir2():
    aux = entrada.get()
    aux = aux + "2"
    entrada.set(aux)
    return entrada

def escribir3():
    aux = entrada.get()
    aux = aux + "3"
    entrada.set(aux)
    return entrada

def escribir4():
    aux = entrada.get()
    aux = aux + "4"
    entrada.set(aux)
    return entrada

def escribir5():
    aux = entrada.get()
    aux = aux + "5"
    entrada.set(aux)
    return entrada

def escribir6():
    aux = entrada.get()
    aux = aux + "6"
    entrada.set(aux)
    return entrada

def escribir7():
    aux = entrada.get()
    aux = aux + "7"
    entrada.set(aux)
    return entrada

def escribir8():
    aux = entrada.get()
    aux = aux + "8"
    entrada.set(aux)
    return entrada

def escribir9():
    aux = entrada.get()
    aux = aux + "9"
    entrada.set(aux)
    return entrada

def escribirMas():
    aux = entrada.get()
    aux = aux + "+"
    entrada.set(aux)
    return entrada

def escribirMenos():
    aux = entrada.get()
    aux = aux + "-"
    entrada.set(aux)
    return entrada
def escribirPor():
    aux = entrada.get()
    aux = aux + "*"
    entrada.set(aux)
    return entrada

def escribirDiv():
    aux = entrada.get()
    aux = aux + "/"
    entrada.set(aux)
    return entrada

def resultado():
    texto = entrada.get()
    lista = []
    for letra in texto:
        lista.append(letra)
    print(lista) #no se como realizar la operacion matematica siendo strings

root = Tk()
root.resizable(0, 0)
marco = Frame(root)
marco.grid(column=0, row=0, padx=(10,10), pady=(10,10))

entrada = StringVar()
entrada.set("")
var = Entry(root, textvariable=entrada)
separador = Label(root, text="")


b0 = Button(root, text="0", command=escribir0, width=5)
b1 = Button(root, text="1", command=escribir1, width=5)
b2 = Button(root, text="2", command=escribir2, width=5)
b3 = Button(root, text="3", command=escribir3, width=5)
b4 = Button(root, text="4", command=escribir4, width=5)
b5 = Button(root, text="5", command=escribir5, width=5)
b6 = Button(root, text="6", command=escribir6, width=5)
b7 = Button(root, text="7", command=escribir7, width=5)
b8 = Button(root, text="8", command=escribir8, width=5)
b9 = Button(root, text="9", command=escribir9, width=5)
b11 = Button(root, text="+", command=escribirMas, width=5)
b12 = Button(root, text="-", command=escribirMenos, width=5)
b13 = Button(root, text="*", command=escribirPor, width=5)
b14 = Button(root, text="/", command=escribirDiv, width=5)
b10 = Button(root, text="=", command=resultado, width=10)

var.grid(column=0, row=0, columnspan=4)
separador.grid(column=0, row=1, columnspan=4)
b0.grid(column=0, row=5)
b1.grid(column=0, row=4)
b2.grid(column=1, row=4)
b3.grid(column=2, row=4)
b4.grid(column=0, row=3)
b5.grid(column=1, row=3)
b6.grid(column=2, row=3)
b7.grid(column=0, row=2)
b8.grid(column=1, row=2)
b9.grid(column=2, row=2)
b10.grid(column=1, row=5, columnspan=2)
b11.grid(column=3, row=2)
b12.grid(column=3, row=3)
b13.grid(column=3, row=5)
b14.grid(column=3, row=4)


root.mainloop()
