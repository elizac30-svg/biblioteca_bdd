import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga tabela ususarios
conn.execute("DROP TABLE IF EXISTS usuarios")

#cria a tabela ususarios
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

#inserindo os registros na tabela ususarios.
conn.executemany("INSERT INTO usuarios(nome) VALUES(?)",
                 [("Jaisusom",), ("Simon",), ("Frodo",),])

#confrimando a criação e os inserts da tabela ususarios.
conn.commit()

