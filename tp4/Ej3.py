import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Vista de árbol en Tkinter")

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


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()