from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Carro import Carro
from comandos_banco import comandos_banco



class interface:

    def __init__(self):
        self.TAMANHO = '1043x453'# declaração de constante para definir o tamanho da pagina
        self.co0 = "#000000"  # Preta
        self.co1 = "#feffff"  # branca
        self.co10 = "#A39D24" #dourado
        self.co11 = "#4714A3" #roxo1
        self.co12 = "#874DF0" #roxo2
        self.co13 = "#FFF86B" #dourado2
        self.co14 = "#F0E94D" #dourado3
        self.co15 = "#333127" #sombra dourado
        self.janela = ''
        self.cont_lista = 0
    
                
    def IniciaInterface(self):
        self.janela = Tk() #cria a janela tk
        self.janela.title("Revenda Automoveis") #titulo da janela
        self.janela.geometry(self.TAMANHO) # tamanho da janela
        self.janela.configure(background=self.co15) #configurando a cor de fundo
        self.janela.resizable(width=False, height=False) #impedir o redimensionamento da janela
        
        comandos_bancos = comandos_banco() #inicia os comandos para o banco de dados
        #CRIANDO OS FRAMES
        frame_cima = Frame(self.janela, width=310, height=50, bg=self.co0, relief='flat') #FRAME PARA LOGO
        frame_cima.grid(row=0, column=0)    

        frame_baixo = Frame(self.janela, width=310, height=403, bg=self.co15, relief='flat') #FRAME PARA INSERIR OS DADOS
        frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1   )

        frame_direita = Frame(self.janela, width=555, height=403, bg=self.co15, relief='flat') #FRAME PARA MOSTRAR OS DADOS
        frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) 

        #inserir os valores
        def inserir():
            #RECUPERAR OS VALORES DAS ENTRYS
            marca = e_marca.get()
            modelo = e_modelo.get()
            ano_fab = e_ano_fab.get()

            if ano_fab.isdigit(): #VERIFICAR SE O ANO DE FABRICAÇÃO É UM NÚMERO, CASO CONTRÁRIO MOSTRAR ERRO
                ano_fab = int(ano_fab)
            else:
                messagebox.showerror('Erro','O ano de fabricação deve ser um número inteiro')
                return False

            preco = e_preco.get()

            if preco.replace('.','', 1).isdigit(): #VERIFICAR SE PRECO É UM NÚMERO, CASO CONTRÁRIO MOSTRAR ERRO
                preco = float(preco)
            else:
                messagebox.showerror('Erro','O preço deve ser um número')
                return False
            
            estado_novo = e_estado_novo.get()
            usado = e_alugado.get()

            carro = Carro(marca, modelo, ano_fab, preco, estado_novo, usado) #criar um objeto para carro

            lista = [carro.getMarca(), carro.getModelo(), carro.getAno_fab(), carro.getPreco(), carro.getEstado_novo(), carro.getAlugado()] #lista para enviar as informações para o banco de dados

            if marca == '' or modelo == '' or ano_fab == '' or preco == '' or estado_novo == '' or usado == '':
                messagebox.showerror('Erro', 'Nenhuma entrada pode estar vazia') #caso algum campo esteja vazio
            else:
                comandos_bancos.inserir_info(lista)
                messagebox.showinfo('Sucesso', 'Informações inseridas com sucesso!') #caso todos os campos estejam preenchidos

                #deletar as entrys
                e_marca.delete(0, 'end')
                e_modelo.delete(0, 'end')
                e_ano_fab.delete(0, 'end')
                e_preco.delete(0, 'end')
                e_estado_novo.delete(0, 'end')
                e_alugado.delete(0, 'end')

            for widget in frame_direita.winfo_children(): #limpar os campos
                widget.destroy()
            Mostrar()
        global tree #variavel tree global

        #atualizar os valores
        def atualizar():
            try:
                treev_dados = tree.focus() #selecionar no lado direito
                treev_dicionario = tree.item(treev_dados) #transformar em dicionario
                tree_lista = treev_dicionario['values'] #transformar em lista

                valor_id = tree_lista[0] #pegar o id

                #deletar as entrys
                e_marca.delete(0, 'end')
                e_modelo.delete(0, 'end')
                e_ano_fab.delete(0, 'end')
                e_preco.delete(0, 'end')
                e_estado_novo.delete(0, 'end')
                e_alugado.delete(0, 'end')

                #colocar nas entrys as informações selecionadas na tree
                e_marca.insert(0, tree_lista[1])
                e_modelo.insert(0, tree_lista[2])
                e_ano_fab.insert(0, tree_lista[3])
                e_preco.insert(0, tree_lista[4])
                e_estado_novo.insert(0, tree_lista[5])
                e_alugado.insert(0, tree_lista[6])


                #função para atualizar as entrys
                def update():
                    marca = e_marca.get()
                    modelo = e_modelo.get()
                    ano_fab = e_ano_fab.get()

                    if ano_fab.isdigit(): #VERIFICAR SE O ANO DE FABRICAÇÃO É UM NÚMERO, CASO CONTRÁRIO MOSTRAR ERRO
                        ano_fab = int(ano_fab)
                    else:
                        messagebox.showerror('Erro','O ano de fabricação deve ser um número inteiro')
                        return False

                    preco = e_preco.get()

                    if preco.replace('.','', 1).isdigit(): #VERIFICAR SE PRECO É UM NÚMERO, CASO CONTRÁRIO MOSTRAR ERRO
                        preco = float(preco)
                    else:
                        messagebox.showerror('Erro','O preço deve ser um número')
                        return False
                    
                    estado_novo = e_estado_novo.get()
                    alugado = e_alugado.get()

                    lista = [marca, modelo, ano_fab, preco, estado_novo, alugado, valor_id] #lista organizada para o banco de dados

                    if marca == '' or modelo == '' or ano_fab == '' or estado_novo == '' or preco == '' or alugado == '':
                        messagebox.showerror('Erro', 'Nenhuma entrada pode estar vazia') #caso algum campo esteja vazio
                    else:
                        lista_preco = [tree_lista[4], preco] #pegar o preço antigo e atual caso aja uma atualização no preço
                        comandos_bancos.atualizar_valor(lista_preco) #atualizar valor para o calulo
                        comandos_bancos.atualizar_info(lista) #atualizar informações
                        messagebox.showinfo('Sucesso', 'Informações atualizadas com sucesso!') #caso todos os campos estejam preenchidos

                        #deletar as entrys
                        e_marca.delete(0, 'end')
                        e_modelo.delete(0, 'end')
                        e_ano_fab.delete(0, 'end')
                        e_preco.delete(0, 'end')
                        e_estado_novo.delete(0, 'end')
                        e_alugado.delete(0, 'end')

                    for widget in frame_direita.winfo_children(): #limpar os campos
                        widget.destroy()

                    Mostrar() #mostrar na tela


                #botão para confirmar a mudança
                b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=7, font=('Ivy 9 bold'), fg='#000000', bg=self.co10, relief='raised', overrelief='ridge')
                b_confirmar.place(x=105, y=370)
                        


            except IndexError: #caso não selecione nenhum elemento
                messagebox.showerror('Erro', 'Escolha um dos dados da tabela')
        #NOME DO APP

        #deletar valores
        def deletar():
            try:
                treev_dados = tree.focus() #selecionar no lado direito
                treev_dicionario = tree.item(treev_dados) #transformar em dicionario
                tree_lista = treev_dicionario['values'] #transformar em lista

                valor_preco = tree_lista[4] #recupera o valor do objeto a ser deletado para atualizar a média de valores
                comandos_bancos.deletar_valor(valor_preco) #deleta o preco da media
                valor_id = [tree_lista[0]] #pegar o id
                comandos_bancos.deletar_info(valor_id) #deleta as informações
                messagebox.showinfo('Sucesso', 'O item foi deletado') #mensagem de sucesso

                for widget in frame_direita.winfo_children(): #limpar os campos
                    widget.destroy()

                Mostrar() #mostrar na tela

            except IndexError: #caso não tenha selecionado nenhum
                messagebox.showerror('Erro', 'Selecione um dos dados da tabela') 

        def MostrarPreco(): #função para o botão de mostrar preço, retorna uma string com o valor médio em uma messagebox
            valor = comandos_bancos.getValor(self.cont_lista)
            return messagebox.showinfo('valor', f'O valor total é: {valor:.2f}')


        #label cima 
        app_nome = Label(frame_cima, text='Revenda Carros', anchor=NW, font=('Ivy 16 bold'), fg=self.co10, bg=self.co0, relief='flat')
        app_nome.place(x=40, y=15) 

        #configurando o frame baixo
        #marca
        l_marca = Label(frame_baixo, text='Marca:', anchor=NW, font=('Ivy 10 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_marca.place(x=15, y=10) 
        e_marca = Entry(frame_baixo, width=35, justify='left', relief='solid')
        e_marca.place(x=15, y=40)

        #modelo
        l_modelo = Label(frame_baixo, text='Modelo:', anchor=NW, font=('Ivy 10 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_modelo.place(x=15, y=70) 
        e_modelo = Entry(frame_baixo, width=35, justify='left', relief='solid')
        e_modelo.place(x=15, y=100)

        #ano de fabricação
        l_ano_fab = Label(frame_baixo, text='Ano de Fabricação:', anchor=NW, font=('Ivy 10 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_ano_fab.place(x=15, y=130) 
        e_ano_fab = Entry(frame_baixo, width=35, justify='left', relief='solid')
        e_ano_fab.place(x=15, y=160)


        #preco
        l_preco = Label(frame_baixo, text='Preço:', anchor=NW, font=('Ivy 10 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_preco.place(x=15, y=190) 
        e_preco = Entry(frame_baixo, width=35, justify='left', relief='solid')
        e_preco.place(x=15, y=220)

        #estado_novo
        l_estado_novo = Label(frame_baixo, text='Novo/Usado:', anchor=NW, font=('Ivy 10 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_estado_novo.place(x=15, y=250) 
        e_estado_novo = Entry(frame_baixo, width=15, justify='left', relief='solid')
        e_estado_novo.place(x=15, y=280)

        #usado
        l_alugado = Label(frame_baixo, text='Alugado:', anchor=NW, font=('Ivy 10 bold'), fg=self.co14, bg=self.co15, relief='flat')
        l_alugado.place(x=160, y=250) 
        e_alugado = Entry(frame_baixo, width=15, justify='left', relief='solid')
        e_alugado.place(x=160, y=280)

        #botão inserir
        b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=7, font=('Ivy 9 bold'), fg=self.co1, bg=self.co11, relief='raised', overrelief='ridge')
        b_inserir.place(x=15, y=340)

        #botão atualizar
        b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=7, font=('Ivy 9 bold'), fg=self.co1, bg=self.co11, relief='raised', overrelief='ridge')
        b_atualizar.place(x=105, y=340)

        #botão deletar
        b_deletar = Button(frame_baixo, text='Deletar', command=deletar, width=7, font=('Ivy 9 bold'), fg=self.co1, bg=self.co11, relief='raised', overrelief='ridge')
        b_deletar.place(x=200, y=340)

        #botão mostrar preço
        b_preco = Button(frame_baixo, command=MostrarPreco, text='Preço Média', width=10, font=('Ivy 9 bold'), fg=self.co1, bg=self.co11, relief='raised', overrelief='ridge')
        b_preco.place(x=15, y=370)

        #função interna para mostrar as informações
        def Mostrar():

            global tree #declara a variavel tree como global

            lista = comandos_bancos.mostrar_info() #adiciona os valores do banco de dados em uma lista 

            # lista para cabecalho
            tabela_head = ['ID','Marca', 'Modelo','Ano Fabricação', 'Preço', 'Usado','Alugado']


            # criando a tabela
            tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

            # barra vertical
            vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

            # barra horizontal
            hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            frame_direita.grid_rowconfigure(0, weight=12)


            hd=["center","center","center","center","center","center","center"] #configurando as direções e tamanhos dos campos do cabeçalho
            h=[30,170,140,100,120,50,100]
            n=0

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=CENTER)
                # ajustas a largura das colunas
                tree.column(col, width=h[n],anchor=hd[n])
                
                n+=1
            self.cont_lista = len(lista)
            for item in lista: #adicionar os itens da lista do banco de dados na tree
                tree.insert('', 'end', values=item)

        Mostrar() #mostrar na tela


        self.janela.mainloop() #loop da janela

    


        