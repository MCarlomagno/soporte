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
        entrada2 = StringVar()
        entrada2.set("")
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
        self.ventanaAgregar = Toplevel()
        self.nombre = StringVar()
        self.dni = StringVar()
        self.apellido = StringVar()

        entradanombre = Entry(self.ventanaAgregar, width=20, textvariable=self.nombre)
        entradaapellido = Entry(self.ventanaAgregar, width=20, textvariable=self.apellido)
        entradadni = Entry(self.ventanaAgregar, width=20, textvariable=self.dni)

        botoncrear = Button(self.ventanaAgregar, text="Agregar",command=self.crear)
        botoncancelar = Button(self.ventanaAgregar, text="Cancelar", command=self.cancelar)

        entradanombre.pack()
        entradaapellido.pack()
        entradadni.pack()
        botoncrear.pack()
        botoncancelar.pack()

    def borrar(self):
        pass

    def editar(self):
        self.ventanaEditar = Toplevel()
        self.nombre = StringVar()
        self.dni = StringVar()
        self.apellido = StringVar()

        entradanombre = Entry(self.ventanaEditar, width=20, textvariable=self.nombre)
        entradaapellido = Entry(self.ventanaEditar, width=20, textvariable=self.apellido)
        entradadni = Entry(self.ventanaEditar, width=20, textvariable=self.dni)

        botonmodificar = Button(self.ventanaEditar, text="Modificar",command=self.modificar)
        botoncancelar = Button(self.ventanaEditar, text="Cancelar", command=self.cancelar)

        entradanombre.pack()
        entradaapellido.pack()
        entradadni.pack()
        botonmodificar.pack()
        botoncancelar.pack()
        pass

    def crear(self):
        pass

    def cancelar(self):
        pass

    def modificar(self):
        pass

principal = tk.Tk()
app = Aplicacion(principal)
app.mainloop()
