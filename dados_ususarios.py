import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")


'''
#---USUÁRIOS---
#apaga tabela ususarios
conn.execute("DROP TABLE IF EXISTS usuarios")

#cria a tabela ususarios
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

#inserindo os registros na tabela ususarios.
conn.executemany("INSERT INTO usuarios(nome) VALUES(?)",
                 [("Jaiusom",), ("Simon",), ("Frodo",),])

conn.executemany("INSERT INTO usuarios(nome) VALUES(?)", \
                 [("The Rock Clark",),("Roberto Cruzez",),])'''

#---EDITORAS---
#apaga tabela editoras
conn.execute("DROP TABLE IF EXISTS editoras")

#cria a tabela editoras
conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

#inserindo os registros na tabela editoras.
conn.executemany("INSERT INTO EDITORAS(nome) VALUES(?)",
                 [("Darkside",), ("Intriseca",), ("Seguinte",),])


#confrimando a criação e os inserts da tabela editoras.
conn.commit()
