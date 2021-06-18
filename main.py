import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3


root = tk()
root.title("Lista de contatos")
width = 800
heigth = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()

root.iconbitmap()
root.config(bg="#6666ff")


nome = StringVar()
telefone = StringVar()
idade = StringVar()
email = StringVar()
endereco = StringVar()


def database():
    conn = sqlite3.connect ("")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NO EXISTS 'humanos' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                nome TEXT, telefone TEXT, idade TEXT, email TEXT, endereco TEXT) """
    cursor.execute(query)
    cursor.execute('SELECT * FROM humanos ORDER BY nome')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def submitData():
    if nome.get() == "" or telefone.get() == "" or idade.get() == "" or email.get() == "" or endereco.get =="":
        resultado = tk.showwarning("", "Pora favor, digitar em todos os campos", icon="warning")
    else:
        conn = sqlite3.connect("")
        cursor = conn.cursor()
        query = """ INSERT INTO 'humanos' (nome, telefone, idade, email, endereço) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get()) ))
        conn.commit()
        cursor.execute('SELECT * FROM humanos ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            nome.set("")
            telefone.set("")
            idade.set("")
            email.set("")
            endereco.set("")

def updateData():
    conn = sqlite3.connect("")
    cursor = conn.cursor()
    query = """ UPDATE  'humanos'  SET nome = ?, telefone = ?, idade = ?, email = ?, endereço = ? WHERE id = ?"""
    cursor.execute(query, (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get()), int(id)))
    conn.commit()
    cursor.execute('SELECT * FROM humanos ORDER BY nome')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    updateWindow.destroy()

def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo["values"]
    id = selectedItem[0]
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    nome.set(selectedItem[1])
    telefone.set(selectedItem[2])
    idade.set(selectedItem[3])
    email.set(selectedItem[4])
    endereco.set(selectedItem[5])

    updateWindow = Toplevel()
    updateWindow.title("ATUALIZANDO CONTATO")
    width = 480
    heigth = 200
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width / 2) - (width / 2)
    y = (sc_height / 2) - (height / 2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    formTitle = Frame(updateWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(updateWindow)
    formContact.pack(side=TOP, pady=10)

    lbl_title = Label(formTitle, text="Atualizando contato", font=('arial', 18), bg='blue', width=300)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(formContact, text="Telefone", font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(formContact, text="Idade", font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(formContact, text="Email", font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(formContact, text="Endereco", font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)

    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    telefoneEntry = Entry(formContact, textvariable=telefone, font=('arial', 12))
    telefoneEntry.grid(row=1, column=1)
    idadeEntry = Entry(formContact, textvariable=idade, font=('arial', 12))
    idadeEntry.grid(row=2, column=1)
    emailEntry = Entry(formContact, textvariable=email, font=('arial', 12))
    emailEntry.grid(row=3, column=1)
    enderecoEntry = Entry(formContact, textvariable=endereco, font=('arial', 12))
    enderecoEntry.grid(row=4, column=1)

    bttn_update = Button(formContact, text="Atualizar", width=50, command=updateData)
    bttn_update.grid(row=6, columnspan=2, pady=10)


def deletarData():
    if not tree.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja deletar o contato?")
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("Nova America/Noite/contatos.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'humanos' WHERE id = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()


def inserirData():
    global newWindow
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")

    newWindow = Toplevel()
    newWindow.title("INSERINDO CONTATO")
    width = 480
    heigth = 200
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width / 2) - (width / 2)
    y = (sc_height / 2) - (height / 2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    formTitle = Frame(newWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(newWindow)
    formContact.pack(side=TOP, pady=10)

    lbl_title = Label(formTitle, text="Inserindo contato",
                      font=('arial', 18), bg='blue', width=300)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(formContact, text="Telefone", font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(formContact, text="Idade", font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(formContact, text="Email", font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(formContact, text="Endereco", font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)

    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    telefoneEntry = Entry(
        formContact, textvariable=telefone, font=('arial', 12))
    telefoneEntry.grid(row=1, column=1)
    idadeEntry = Entry(formContact, textvariable=idade, font=('arial', 12))
    idadeEntry.grid(row=2, column=1)
    emailEntry = Entry(formContact, textvariable=email, font=('arial', 12))
    emailEntry.grid(row=3, column=1)
    enderecoEntry = Entry(
        formContact, textvariable=endereco, font=('arial', 12))
    enderecoEntry.grid(row=4, column=1)

    bttn_inserir = Button(formContact, text="Inserir",
                          width=50, command=submitData)
    bttn_inserir.grid(row=6, columnspan=2, pady=10)


def sobreApp():
    pass

top = Frame(root, width=500, bd=1,relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg="#6666ff")
mid.pack(side=TOP)
midLeft = Frame(mid, width=100)
midLeft.pack(side=LEFT)
midLeftPadding = Frame(mid, width=350, bg="#6666ff")
midLeftPadding.pack(side=LEFT)
midRight = Frame(mid, width=100)
midRight.pack(side=RIGHT)
bottom = Frame(root, width=200)
bottom.pack(side=BOTTOM)
tableMargim = Frame(root, width=500)
tableMargim.pack(side=TOP)

lbl_title = Label(top, text="SISTEMA DE GERENCIAMENTO DE CONTATOS", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alt = Label(bottom, text="Para alterar clique duas vezes no contato desejado.", font=('arial', 12), width=200)
lbl_alt.pack(fill=X)

bttn_add = Button(midLeft, text="Inserir", bg="OliveDrab1", command=inserirData)
bttn_add.pack()
bttn_del = Button(midRight, text="Deletar",
                 bg="orange red", command=deletarData)
bttn_del.pack(side=RIGHT)

scrollbarX = Scrollbar(tableMargim, orient=HORIZONTAL)
scrollbarY = Scrollbar(tableMargim, orient=VERTICAL)

tree = ttk.Treeview(tableMargim, columns=("ID", "Nome", "Telefone", "Idade", "Email", "Endereço"), height=400,
                    selectmode="extended", yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
scrollbarY.config(command=tree.yview)
scrollbarY.pack(side=RIGHT, fill=Y)
scrollbarX.config(command=tree.xview)
scrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Telefone", text="Telefone", anchor=W)
tree.heading("Idade", text="Idade", anchor=W)
tree.heading("Email", text="Email", anchor=W)
tree.heading("Endereço", text="Endereço", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)

menu_bar = Menu(root)
root.config(menu=menu_bar)

fileMenu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="Menu", menu=fileMenu)
fileMenu.add_command(label="Criar Novo", command=inserirData)
fileMenu.add_separator()
fileMenu.add_command(label="Sair", command=root.destroy)

menuSobre = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="Sobre", menu=menuSobre)
menuSobre.add_command(label="Info", command=sobreApp)

if __name__ == '__main__':
    database()
    root.mainloop()