import tkinter as tk
from tkinter import *
from tkinter import ttk


class Aplicacion(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)
        principal.title("Vista de árbol")

        self.treeview = ttk.Treeview(self)
        self.treeview.pack()
        ros = self.treeview.insert("", tk.END, text="Rosario")
        self.treeview.insert(ros, tk.END, text="2000")
        bsas = self.treeview.insert("", tk.END, text="Buenos Aires")
        self.treeview.insert(bsas, tk.END, text="2001")
        cor = self.treeview.insert("", tk.END, text="Cordoba")
        self.treeview.insert(cor, tk.END, text="2003")
        sal = self.treeview.insert("", tk.END, text="Salta")
        self.treeview.insert(sal, tk.END, text="2004")
        san = self.treeview.insert("", tk.END, text="San Salvador")
        self.treeview.insert(san, tk.END, text="2005")
        self.pack()

        b1 = Button(root, text="Alta",command=self.agregar)
        b2 = Button(root, text="Baja", command= self.borrar)
        b3 = Button(root, text="Modificar", command = self.editar)
        entrada1 = StringVar()
        entrada1.set("")
        self.campo1 = Entry(root, textvariable = entrada1)
        entrada2 = StringVar()
        entrada2.set("")
        self.campo2 = Entry(root, textvariable = entrada2)

        etiq1 = Label(root, text="ingresar ciudad")
        etiq1.pack()
        self.campo1.pack()
        etiq2 = Label(root, text="ingresar codigo postal")
        etiq2.pack()
        self.campo2.pack()
        b1.pack()
        b2.pack()
        b3.pack()

    def agregar(self):
        ciudad = self.treeview.insert("", tk.END, text=self.campo1.get())
        self.treeview.insert(ciudad, tk.END, text=self.campo2.get())

    def borrar(self):
        item = self.treeview.selection()[0]
        self.treeview.delete(item)

    def editar(self):
        item = self.treeview.selection()[0]
        self.treeview.item(item, text=self.campo1.get())
        hijo = self.treeview.get_children(item)
        self.treeview.item(hijo, text=self.campo2.get())

principal = tk.Tk()
app = Aplicacion(principal)
app.mainloop()