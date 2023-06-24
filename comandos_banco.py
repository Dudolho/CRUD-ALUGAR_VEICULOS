import sqlite3 as lite

class comandos_banco:
#criando conexão 
    def __init__(self):
        self.con = lite.connect('dados.db')
        f = open('valor.txt', 'r')
        self.valor = f.read()
        self.valor = float(self.valor)
        f.close()


    #inserir
    def inserir_info(self, i):
        with self.con:
            cur = self.con.cursor()
            query = "INSERT INTO formulario (marca, modelo, ano_fab, preco, estado_novo, alugado) VALUES(?, ?, ?, ?, ?, ?)"
            cur.execute(query, i)
        valor = float(i[3])
        self.valor += valor
        f = open('valor.txt', 'w')
        f.write(str(self.valor))
        f.close()


    #mostar
    def mostrar_info(self):
        lista = []
        with self.con:
            cur = self.con.cursor()
            query = "SELECT * FROM formulario"
            cur.execute(query)
            info = cur.fetchall()
            
            for i in info:
                lista.append(i)
        return lista




    #update
    def atualizar_info(self, i):
        with self.con:
            cur = self.con.cursor()
            query = "UPDATE formulario SET marca=?, modelo=?, ano_fab=?, preco=?, estado_novo=?, alugado=? WHERE id=?"
            cur.execute(query, i)
  
    def atualizar_valor(self, i):
        valor_antigo = float(i[0])
        valor_novo = float(i[1])
        self.valor -= valor_antigo
        self.valor += valor_novo
        f = open('valor.txt', 'w')
        f.write(str(self.valor))
        f.close()



    #deletar
    def deletar_info(self, i):
        with self.con:
            cur = self.con.cursor()
            query = "DELETE FROM formulario WHERE id=?"
            cur.execute(query, i)
    
    def deletar_valor(self, i):
        valor = float(i)
        self.valor -= valor
        f = open('valor.txt', 'w')
        f.write(str(self.valor))
        f.close()
    
    #get do valor:
    def getValor(self, tamanho_lista):
        return self.valor / tamanho_lista
            