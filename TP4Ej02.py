from tkinter import *


def escribir(cuenta, dato):
    aux = str(cuenta.get())
    aux = aux + str(dato)
    cuenta.set(aux)

def ok(cuenta):
    aux = eval(str(cuenta.get()))
    cuenta.set(aux)

def l0():
    escribir(entrada, "0")

def l1():
    escribir(entrada, "1")

def l2():
    escribir(entrada, "2")

def l3():
    escribir(entrada, "3")

def l4():
    escribir(entrada, "4")

def l5():
    escribir(entrada, "5")

def l6():
    escribir(entrada, "6")

def l7():
    escribir(entrada, "7")

def l8():
    escribir(entrada, "8")

def l9():
    escribir(entrada, "9")

def l10():
    ok(entrada)

def l11():
    escribir(entrada, "+")

def l12():
    escribir(entrada, "-")

def l13():
    escribir(entrada, "*")

def l14():
    escribir(entrada, "/")

root = Tk()
root.resizable(0, 0)
marco = Frame(root)
marco.grid(column=0, row=0, padx=(10,10), pady=(10,10))

entrada = StringVar()
entrada.set("")
var = Entry(root, textvariable=entrada)
separador = Label(root, text="")


b0 = Button(root, text="0", command=l0, width=5)
b1 = Button(root, text="1", command=l1, width=5)
b2 = Button(root, text="2", command=l2, width=5)
b3 = Button(root, text="3", command=l3, width=5)
b4 = Button(root, text="4", command=l4, width=5)
b5 = Button(root, text="5", command=l5, width=5)
b6 = Button(root, text="6", command=l6, width=5)
b7 = Button(root, text="7", command=l7, width=5)
b8 = Button(root, text="8", command=l8, width=5)
b9 = Button(root, text="9", command=l9, width=5)
b11 = Button(root, text="+", command=l11, width=5)
b12 = Button(root, text="-", command=l12, width=5)
b13 = Button(root, text="*", command=l13, width=5)
b14 = Button(root, text="/", command=l14, width=5)
b10 = Button(root, text="=", command=l10, width=10)

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
