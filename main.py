from tkinter import *
from tkinter import ttk
import webbrowser
root = Tk()

mylabel1 = Label(root, fg='gold', bg='#856ff8', text="Cześć")
mylabel2 = Label(root,bg='#856ff8', text="JESTEM SZYMEK")
mylabel3 = Label(root, bg='#856ff8', text="a oto moja strona internetowa")


mylabel1.grid(row=0, column=3)
mylabel2.grid(row=1, column=3)
mylabel3.grid(row=2, column=3)
wyjscie = ttk.Button(root, text="wyjdz", command=root.destroy).grid(column=6, row=3)
moja_strona = ttk.Button(root, text="odwiedz moja strone", command=lambda:webbrowser.open("https://s2.kozaczek.pl/wp-content/uploads/sites/2/2021/05/30/wersow-powiekszyla-piersi.jpg")).grid(column=2, row=3)


mylabel1["fg"] = "gold"


root.geometry("400x200")
root.configure(bg='#856ff8')
root.mainloop()