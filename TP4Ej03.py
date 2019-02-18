from tkinter import *
from tkinter import ttk

root = Tk()

columns = ('Ciudad', 'Código Postal')
tree = ttk.Treeview(columns=columns, show='headings')
for clm in columns:
        tree.heading(clm, text=clm)

tree.insert('', 'end',  values=("Rosario","2000"),iid=1)
tree.insert('', 'end',  values=("Resistencia","3500"),iid=2)
tree.insert('', 'end',  values=("Casilda","2170"),iid=3)
tree.insert('', 'end',  values=("Reconquista","3560"),iid=4)
tree.insert('', 'end',  values=("Eldorado","3380"),iid=5)

tree.pack()

root.mainloop()
