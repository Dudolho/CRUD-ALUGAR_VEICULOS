from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from interface import interface

class Login_page:
    def __init__(self):
        self.TAMANHO = '600x400'
        self.co0 = "#000000"  # Preta
        self.co1 = "#feffff"  # branca
        self.co10 = "#A39D24" #dourado
        self.co11 = "#4714A3" #roxo1
        self.co12 = "#874DF0" #roxo2
        self.co13 = "#FFF86B" #dourado2
        self.co14 = "#F0E94D" #dourado3
        self.co15 = "#333127" #sombra dourado
        self.janela=''
        self.email = '123'
        self.senha = '123'
        self.acesso = False

    def IniciaLoginPage(self):
        self.janela = Tk() #cria a janela tk
        self.janela.title("Revenda Automoveis") #titulo da janela
        self.janela.geometry(self.TAMANHO) # tamanho da janela
        self.janela.configure(background=self.co15) #configurando a cor de fundo
        self.janela.resizable(width=False, height=False) #impedir o redimensionamento da janela

        def entrar():
            email = e_email.get()
            senha = e_senha.get()

            if email == self.email and senha == self.senha:
                self.janela.destroy()
                janela = interface()
                janela.IniciaInterface()
            
            else:
                messagebox.showerror('Erro', 'senha ou email incorretos!')
                e_email.delete(0, 'end')
                e_senha.delete(0, 'end')
        #CRIANDO OS FRAMES
        frame_cima = Frame(self.janela, width=600, height=100, bg=self.co0, relief='flat') #FRAME PARA LOGO
        frame_cima.grid(row=0, column=0) 


        frame_baixo = Frame(self.janela, width=600, height=300, bg=self.co15, relief='flat') #FRAME PARA INSERIR OS DADOS
        frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1   )


        l_logo = Label(frame_cima, text='LOGIN FUNCIONARIO', anchor=NW, font=('Ivy 25 bold'), fg=self.co10, bg=self.co0, relief='flat')
        l_logo.place(x=130, y=30)


        l_email = Label(frame_baixo, text='Email:', anchor=NW, font=('Ivy 12 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_email.place(x=200, y=50) 
        e_email = Entry(frame_baixo, width=35, justify='left', relief='solid')
        e_email.place(x=200, y=80)

        l_senha = Label(frame_baixo, text='Senha:', anchor=NW, font=('Ivy 12 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_senha.place(x=200, y=110) 
        e_senha = Entry(frame_baixo, width=35, justify='left', relief='solid', show='*')
        e_senha.place(x=200, y=140)

        b_entrar = Button(frame_baixo, text='ENTRAR', command=entrar, width=7, font=('Ivy 9 bold'), fg=self.co1, bg=self.co11, relief='raised', overrelief='ridge')
        b_entrar.place(x=200, y=170)

        self.janela.mainloop()
