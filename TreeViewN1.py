from Tkinter import *
import ttk

root = Tk()
label = Label(root,text="ABM Socio")
button = Button(root,text="Alta")

columns = ('Ciudad', 'Codigo Postal')
##tree = ttk.Treeview()
tree = ttk.Treeview( columns=columns, show='headings')
##tree.place(relx=0.02, rely=0.04, relheight=0.79, relwidth=0.96)
for clm in columns:
        tree.heading(clm, text=clm)

###***tree.insert('Rosario','2000')
tree.insert('', 'end',  values=("Rosario","2000"),iid=1)
tree.insert('', 'end',  values=("Resistencia","1000"),iid=2)
tree.insert('', 'end',  values=("Casilda","3000"),iid=3)
tree.insert('', 'end',  values=("Reconquista","4000"),iid=4)
tree.insert('', 'end',  values=("ElDorado","5000"),iid=5)

tree.item(1,values=("FUNES","2001"))


label.pack()
button.pack()
tree.pack()

root.mainloop()
