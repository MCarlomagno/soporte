import tkinter as tkinter
from tkinter import ttk


class Marco(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Ej 4")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        self.ciudad_label = tkinter.Label(self.parent, text ="Ciudad:")
        self.ciudad_entry = tkinter.Entry(self.parent)
        self.ciudad_label.grid(row=0, column=0, sticky=tkinter.W)
        self.ciudad_entry.grid(row=0, column=1)

        self.cp_label = tkinter.Label(self.parent, text="Código postal:")
        self.cp_entry = tkinter.Entry(self.parent)
        self.cp_label.grid(row=1, column=0, sticky=tkinter.W)
        self.cp_entry.grid(row=1, column=1)

        self.alta_button = tkinter.Button(self.parent, text="Alta", command=self.insert_data)
        self.alta_button.grid(row=2, column=1, sticky=tkinter.W)
        self.salir_button = tkinter.Button(self.parent, text="Salir", command=self.parent.quit)
        self.salir_button.grid(row=0, column=3)

        self.tree = ttk.Treeview( self.parent, columns=('Ciudad', 'Código postal'))
        self.tree.heading('#1', text='Ciudad')
        self.tree.heading('#2', text='Código postal')
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

    def insert_data(self):
        self.treeview.insert('', 'end', values=(self.ciudad_entry.get(), self.cp_entry.get()))


def main():
    root = tkinter.Tk()
    m = Marco(root)
    root.mainloop()


if __name__ == "__main__":
    main()
