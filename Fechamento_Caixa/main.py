from tkinter import *


#FUNCTIONS
def novo_caixa():
    print("Novo")
    import novo
    open('novo.py', 'r')


def consultar():
    print("Consultar")

def editar():
    print("editar")

def sair():
    print("Sair")
    exit()

janelaMain = Tk()
janelaMain.title('Fechamento do Caixa - Papelaria Central')

#WINDOW WIDGET'S

# MAIN TEXT
lb1 = Label(janelaMain, text="Fechamento do Caixa", font=("tahoma", 16), bg="light blue")
lb1.pack(fill=X)

# sub TEXT
lb2 = Label(janelaMain, text="Menu Inicial", font=("tahoma", 14))
lb2.place(x=100, y=30)
lb2.pack(fill=X)

# Botão NOVO
bt1 = Button(janelaMain, width=20, text="Novo", command=novo_caixa)
bt1.place(x=100, y=80)

# Botão Consultar
bt2 = Button(janelaMain, width=20, text="Consultar", command=consultar)
bt2.place(x=100, y=110)

# Botão Editar
bt3 = Button(janelaMain, width=20, text="Editar", command=editar)
bt3.place(x=100, y=140)

# Botão Sair
bt4 = Button(janelaMain, width=20, text='SAIR', foreground="red", command=sair )
bt4.place(x=100, y=310)

janelaMain.geometry("350x350+400+120")
janelaMain.mainloop()