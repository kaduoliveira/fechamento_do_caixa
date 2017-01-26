from tkinter import *

#FUNCTIONS

def novo_caixa():

    def salvar():
        print("Salvar")

    def voltar():
        print("Voltar")
        janelaNovo.destroy()

    print("Menu Inicial --> Cadastro de Novo Caixa")
    janelaNovo = Tk()
    janelaNovo.title('Fechamento do Caixa - Papelaria Central')

    # LABELS
    lb_tituloJanela = Label(janelaNovo, text="Fechamento do Caixa", font=("tahoma", 16), bg="light blue")
    lb_subTituloJanelaNovo = Label(janelaNovo, text="Cadastro de Novo Caixa", font=("tahoma", 14))
    lb_diaDaSemana = Label(janelaNovo, text="DOM", bg="light yellow") #Deve ser preenchido automaticamente, de acordo com a data e deve se armazenada
    lb_data = Label(janelaNovo, text="Data:")

    lb_tituloJanela.pack(fill=X)
    lb_subTituloJanelaNovo.place(x=100, y=30)
    lb_subTituloJanelaNovo.pack(fill=X)
    lb_diaDaSemana.place(x=530, y=70)
    lb_data.place(x=360, y=70)

    # BUTTONS
    bt_salvar = Button(janelaNovo, width=20, text="Salvar", command=salvar)
    bt_voltar = Button(janelaNovo, width=20, text='Voltar', command=voltar)

    bt_salvar.place(x=240, y=500)
    bt_voltar.place(x=240, y=560)

    # Campo DATA
    en_data = Entry(janelaNovo)
    en_diaDaSemana = Entry(janelaNovo)

    en_data.place(x=400, y=70)
    en_diaDaSemana.place(x=400, y=150)

    # WNDOW GEOMETRY
    janelaNovo.geometry("600x600+280+80")
    janelaNovo.mainloop()

def consultar():

    def voltar():
        print("Voltar")
        janelaConsulta.destroy()


    print("Menu Inicial ---> Consultar")

    janelaConsulta = Tk()
    janelaConsulta.title("Fechamento do Caixa - Consulta")

    separator = Frame(janelaConsulta, height=400, width=500, bd=1, relief=SUNKEN, bg="white", borderwidth="2")
    separator.place(x=50, y=100)

    #LABELS
    lb_tituloJanelaConsulta = Label(janelaConsulta, text="Consultar Fechamento do Caixa", font=("tahoma", 14))
    lb_campoConsulta = Label(janelaConsulta, text="Insira a data:", font=(13))

    lb_tituloJanelaConsulta.pack(anchor="n")
    lb_campoConsulta.place(x=30, y=50)

    #ENTRY
    en_campoConsulta = Entry(janelaConsulta)

    en_campoConsulta.place(x=130, y=53)

    #BUTTONS
    bt_voltar = Button(janelaConsulta, width=20, text='Voltar', command=voltar)

    bt_voltar.place(x=240, y=560)

    # WNDOW GEOMETRY
    janelaConsulta.geometry("600x600+280+80")
    janelaConsulta.mainloop()

def editar():

    def voltar():
        print("Voltar")
        janelaEditar.destroy()

    print("Menu Inicial ---> Editar")

    #WINDOW
    janelaEditar = Tk()
    janelaEditar.title("Editar - Fechamento de Caixa")


    # BUTTONS
    bt_voltar = Button(janelaEditar, width=10, text='Voltar', command=voltar)
    bt_salvar = Button(janelaEditar, width=20, text="Salvar", foreground="blue")

    bt_voltar.place(x=500, y=560)
    bt_salvar.place(x=330, y=560)


    # WNDOW GEOMETRY
    janelaEditar.geometry("600x600+280+80")
    janelaEditar.mainloop()

def acessoEditar():

    def voltar():
        print("Voltar")
        janelaSenha.destroy()


    def bt_senha_click():
        senha_ed = en_senha.get()
        if senha_ed == '123':
            janelaSenha.destroy()
            editar()
        else:
            voltar()


    print("senha")
    janelaSenha = Tk()
    janelaSenha.title("Senha de Acesso")
    janelaSenha.focus_force()


    en_senha = Entry(janelaSenha, width=20)
    en_senha.place(x=150, y=70)
    en_senha.focus_force()

    lb_tituloJanelaSenha = Label(janelaSenha, text="Insira a senha para editar os relatórios", font=("Calibri", 14), foreground="blue")
    lb_tituloJanelaSenha.pack(anchor="n")

    bt_senha = Button(janelaSenha, width=15, text="Acessar", command=bt_senha_click)
    bt_senha.place(x=150, y=100)

    bt_voltar = Button(janelaSenha, width=15, text="Voltar", command=voltar)
    bt_voltar.place(x=150, y=140)

    janelaSenha.geometry("400x200+400+160")
    janelaSenha.mainloop()

def sair():
    print("Sair")
    exit()

janelaMain = Tk()
janelaMain.title('Fechamento do Caixa - Papelaria Central')

# LABEL'S JanelaMain
lb_tituloJanelaMain = Label(janelaMain, text="Fechamento do Caixa", font=("tahoma", 16), bg="light blue")
lb_subTituloJanelaMain = Label(janelaMain, text="Menu Inicial", font=("tahoma", 14))


lb_tituloJanelaMain.pack(fill=X)

# sub TEXT

lb_subTituloJanelaMain.place(x=100, y=30)
lb_subTituloJanelaMain.pack(fill=X)

# Botão NOVO
bt1 = Button(janelaMain, width=20, text="Novo", command=novo_caixa)
bt1.place(x=100, y=80)

# Botão Consultar
bt2 = Button(janelaMain, width=20, text="Consultar", command=consultar)
bt2.place(x=100, y=110)

# Botão Editar
bt3 = Button(janelaMain, width=20, text="Editar", command=acessoEditar)
bt3.place(x=100, y=140)

# Botão Sair
bt4 = Button(janelaMain, width=20, text='SAIR', foreground="red", command=sair )
bt4.place(x=100, y=310)

janelaMain.geometry("350x350+400+120")
janelaMain.mainloop()