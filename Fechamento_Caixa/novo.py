from tkinter import *

#FUNCTIONS
def cadastrar():
    print("Cadastrar")

def voltar():
    print("Voltar")
    janelaNovo.destroy()



janelaNovo = Tk()
janelaNovo.title('Fechamento do Caixa - Papelaria Central')

#WINDOW WIDGET'S

# MAIN TEXT
lb1 = Label(janelaNovo, text="Fechamento do Caixa", font=("tahoma", 16), bg="light blue")
lb1.pack(fill=X)

# sub TEXT
lb2 = Label(janelaNovo, text="Cadastro de Novo Caixa", font=("tahoma", 14))
lb2.place(x=100, y=30)
lb2.pack(fill=X)

# Botão CADASTRAR
bt_cadastrar = Button(janelaNovo, width=20, text="Cadastrar", command=cadastrar)
bt_cadastrar.pack(side=BOTTOM)

# Botão Voltar
bt_voltar = Button(janelaNovo, width=20, text='Voltar', command=voltar)
bt_voltar.pack(side=BOTTOM)

# Entrada de DADOS

# Campo DATA
data = Entry(janelaNovo)
data.place(x=100, y=120)


janelaNovo.geometry("600x600+280+80")
janelaNovo.mainloop()
