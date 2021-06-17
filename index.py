import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3

root = Tk()
root.title(" SISTEMAS DE NOTA DA ESTÁCIO DE SÁ")
width = 900
height = 600
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)
root.config(bg='gray90')


nome  = StringVar()
notaAv1 = StringVar()
notaAv2 = StringVar()
notaAv3 = StringVar()
avd = StringVar()
avds = StringVar()
id = None
updateWindow = None
newWindow = None



def database():
    conn = sqlite3.connect("./trabalho.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'notas' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT, av1 TEXT, av2 TEXT, av3 TEXT, avd TEXT, avds TEXT) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'notas' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def submitData():
    if nome.get() == "" or notaAv1.get() == "" or notaAv2.get() == "" or notaAv3.get() == "" or avd.get() == "" or avds.get() == "":
        resultado = msb.showwarning(
            "", "Por favor, selecione 'X' no campo quando não necessitar da AV3 e AVDS.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("./trabalho.db")
        cursor = conn.cursor()
        query = """ INSERT INTO 'notas' (nome, av1, av2, av3, avd, avds) VALUES(?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(notaAv1.get()), str(
            notaAv2.get()), str(notaAv3.get()), str(avd.get()), str(avds.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'notas' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        notaAv1.set("")
        notaAv2.set("")
        notaAv3.set("")
        avd.set("")
        avds.set("")
        


def updateData():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("./trabalho.db")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE 'notas' SET nome = ?, av1 = ?, av2 = ?, av3 = ?, avd = ?, avds = ? WHERE id = ?""",
                   (str(nome.get()), str(notaAv1.get()), str(notaAv2.get()), str(notaAv3.get()), str(avd.get()), str(avds.get()), int(id)))
    conn.commit()
    cursor.execute("SELECT * FROM 'notas' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    notaAv1.set("")
    notaAv2.set("")
    notaAv3.set("")
    avd.set("")
    avds.set("")
    updateWindow.destroy()


def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo['values']
    id = selectedItem[0]
    nome.set("")
    notaAv1.set("")
    notaAv2.set("")
    notaAv3.set("")
    avd.set("")
    avds.set("")
    

    nome.set(selectedItem[1])
    notaAv1.set(selectedItem[2])
    notaAv2.set(selectedItem[3])
    notaAv3.set(selectedItem[4])
    avd.set(selectedItem[5])
    avds.set(selectedItem[6])
    
    updateWindow = Toplevel()
    updateWindow.title("    ATUALIZAR NOTA    ")
    formTitulo = Frame(updateWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(updateWindow, bg="gray90")
    formContato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)
    updateWindow.config(bg="gray90")

    lbl_title = Label(formTitulo, text="Atualizar Nota",
                      font=('arial', 18, "bold"), bg='gray0', fg="snow", width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Disciplina:', bg="gray90", font=('arial', 12, "bold"))
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(formContato, text='AV1:', bg="gray90", font=('arial', 12, "bold"))
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2= Label(formContato, text='AV2:', bg="gray90", font=('arial', 12, "bold"))
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(formContato, text='AV3:', bg="gray90", font=('arial', 12, "bold"))
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(formContato, text='AVD:', bg="gray90", font=('arial', 12, "bold"))
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(formContato, text='AVDS:',bg="gray90",  font=('arial', 12, "bold"))
    lbl_avds.grid(row=5, sticky=W)
   

    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    av1Entry = Entry(formContato, textvariable=notaAv1, font=('arial', 12))
    av1Entry.grid(row=1, column=1)
    av2Entry = Entry(formContato, textvariable=notaAv2, font=('arial', 12))
    av2Entry.grid(row=2, column=1)
    av3Entry = Entry(formContato, textvariable=notaAv3, font=('arial', 12))
    av3Entry.grid(row=3, column=1)
    avdEntry = Entry(formContato, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=4, column=1)
    avdsEntry = Entry(formContato, textvariable=avds, font=('arial', 12))
    avdsEntry.grid(row=5, column=1)
  
    bttn_updatecom = Button(formContato, text="Atualizar",
                            width=40, bd=0, fg="snow", bg="DodgerBlue3", command=updateData, font=('arial', 10, 'bold'), pady=5)
    bttn_updatecom.grid(row=6, columnspan=2, pady=10)


def deleteData():
    if not tree.selection():
        resultado = msb.showwarning(
            '', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion(
            '', 'Tem certeza que deseja deletar a disciplina?')
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("./trabalho.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'notas' WHERE id = %d" %
                           selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()


def insertData():
    global newWindow
    nome.set("")
    notaAv1.set("")
    notaAv2.set("")
    notaAv3.set("")
    avd.set("")
    avds.set("")
    
  


    newWindow = Toplevel()
    newWindow.title("    INSERIR NOTA    ")
    formTitulo = Frame(newWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(newWindow, bg='gray90')
    formContato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)
    newWindow.config(bg='gray90')

    lbl_title = Label(formTitulo, text="Inserir Nota", font=('arial', 18, "bold"), bg='gray0', fg="snow", width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Disciplina:', font=('arial', 12, "bold"), bg='gray90')
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(formContato, text='Av1:', font=('arial', 12, "bold"), bg='gray90')
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2 = Label(formContato, text='Av2:', font=('arial', 12, "bold"), bg='gray90')
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(formContato, text='Av3:', font=('arial', 12, "bold"), bg='gray90')
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(formContato, text='Avd:', font=('arial', 12, "bold"), bg='gray90')
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(formContato, text='Avds:', font=('arial', 12, "bold"), bg='gray90')
    lbl_avds.grid(row=5, sticky=W)

    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    av1Entry = Entry(
        formContato, textvariable=notaAv1, font=('arial', 12))
    av1Entry.grid(row=1, column=1)
    av2Entry = Entry(formContato, textvariable=notaAv2, font=('arial', 12))
    av2Entry.grid(row=2, column=1)
    av3Entry = Entry(formContato, textvariable=notaAv3, font=('arial', 12))
    av3Entry.grid(row=3, column=1)
    avdEntry = Entry(formContato, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=4, column=1)
    avdsEntry = Entry(formContato, textvariable=avds, font=('arial', 12))
    avdsEntry.grid(row=5, column=1)

    bttn_submitcom = Button(formContato, text="Cadastrar",
                            width=40, command=submitData, bg="sea green", fg="snow", bd=0, pady=5, font=('arial', 10, 'bold'))
    bttn_submitcom.grid(row=6, columnspan=2, pady=10)


top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg='gray90')
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=10)
midleftPadding = Frame(mid, width=350, bg="gray90")
midleftPadding.pack(side=LEFT)
midright = Frame(mid, width=100)
midright.pack(side=RIGHT, pady=10)
bottom = Frame(root, width=500)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

lbl_title = Label(top, text="SISTEMA DE NOTAS", font=('arial', 18, "bold"), width=500, bg="gray1", fg="snow", pady=10)
lbl_title.pack(fill=X)

lbl_alterar = Label(bottom, text="Para alterar clique duas vezes no contato desejado.", font=('arial', 12), width=200, pady=20, bg="gray1", fg="snow")
lbl_alterar.pack(fill=X)

bttn_add = Button(midleft, text="Inserir", bg="sea green", command=insertData, bd=0, pady=8, padx=20, font=('arial', 10, 'bold'), fg="snow")
bttn_add.pack()
bttn_delete = Button(midright, text="Deletar", bg="IndianRed4", command=deleteData, bd=0, pady=8, padx=20, font=('arial', 10, 'bold'), fg="snow")
bttn_delete.pack(side=RIGHT)

ScrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Disciplina", "AV1", "AV2", "AV3", "AVD", "AVDS"),
                    height=400, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand = ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Disciplina", text="Disciplina", anchor=W)
tree.heading("AV1", text="AV1", anchor=W)
tree.heading("AV2", text="AV2", anchor=W)
tree.heading("AV3", text="AV3", anchor=W)
tree.heading("AVD", text="AVD", anchor=W)
tree.heading("AVDS", text="AVDS", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=30)
tree.column('#2', stretch=NO, minwidth=0, width=170)
tree.column('#3', stretch=NO, minwidth=0, width=60)
tree.column('#4', stretch=NO, minwidth=0, width=60)
tree.column('#5', stretch=NO, minwidth=0, width=60)
tree.column('#6', stretch=NO, minwidth=0, width=60)
tree.column('#7', stretch=NO, minwidth=0, width=60)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)

database()
root.mainloop()