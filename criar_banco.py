#importando sqlite3
import sqlite3 as lite

# criando conexção
con = lite.connect('dados.db')


#criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, marca TEXT, modelo TEXT, ano_fab TEXT, preco DOUBLE, estado_novo TEXT, alugado TEXT)")