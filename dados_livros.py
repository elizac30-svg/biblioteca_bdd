import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")


#apaga tabela ususarios
conn.execute("DROP TABLE IF EXISTS livros")

#cria a tabela ususarios
conn.execute("CREATE TABLE livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL / \
             autor_id INTEGER REFERENCES autor(id),  ")

#inserindo os registros na tabela ususarios.
conn.executemany("INSERT INTO usuarios(nome) VALUES(?)",
                 [("Jaiusom",), ("Simon",), ("Frodo",),])


#confrimando a criação e os inserts da tabela editoras.
conn.commit()