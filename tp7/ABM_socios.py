import tkinter as tk
from tkinter import *
from tkinter import ttk


class Aplicacion(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)
        principal.title("Vista de árbol")

        self.treeview = ttk.Treeview(self, columns=("nombre","apellido","DNI"))
        self.treeview.heading("#0",text="Id")
        self.treeview.heading("nombre", text="Nombre")
        self.treeview.heading("apellido", text="Apellido")
        self.treeview.heading("DNI", text="DNI")
        self.treeview.pack()

        bool = False
        bool = self.cargarTreeView()
        if(bool):
            print("treeview cargada con exito")


        b1 = Button(root, text="Alta",command=self.agregar)
        b2 = Button(root, text="Baja", command= self.borrar)
        b3 = Button(root, text="Modificar", command = self.editar)
        entrada1 = StringVar()
        entrada1.set("")
        #self.campo1 = Entry(root, textvariable = entrada1)
        entrada2 = StringVar()
        entrada2.set("")
        #self.campo2 = Entry(root, textvariable = entrada2)

        #etiq1 = Label(root, text="ingresar ciudad")
        #etiq1.pack()
        #self.campo1.pack()
        #etiq2 = Label(root, text="ingresar codigo postal")
        #etiq2.pack()
        #self.campo2.pack()
        b1.pack()
        b2.pack()
        b3.pack()

    def cargarTreeView(self):
        ros = self.treeview.insert("" ,tk.END,text="1", values=("marcos", "carlomagno", "38596098"))
        ros = self.treeview.insert("", tk.END,text="1", values=("marcos", "carlomagno", "38596098"))
        ros = self.treeview.insert("", tk.END,text="1", values=("marcos", "carlomagno", "38596098"))
        ros = self.treeview.insert("", tk.END,text="1", values=("marcos", "carlomagno", "38596098"))
        ros = self.treeview.insert("", tk.END,text="1", values=("marcos", "carlomagno", "38596098"))
        self.pack()
        return True

    def agregar(self):
        pass
        #ciudad = self.treeview.insert("", tk.END, text=self.campo1.get())
        #self.treeview.insert(ciudad, tk.END, text=self.campo2.get())

    def borrar(self):
        pass
        #item = self.treeview.selection()[0]
        #self.treeview.delete(item)

    def editar(self):
        pass
        #item = self.treeview.selection()[0]
       # self.treeview.item(item, text=self.campo1.get())
        #hijo = self.treeview.get_children(item)
        #self.treeview.item(hijo, text=self.campo2.get())


principal = tk.Tk()
app = Aplicacion(principal)
app.mainloop()