import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTs livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    título TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT 
)

""")

def adicionar_livro(titulo, autor, ano):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano)
        VALUES (?, ?, ?)
        """,
        (titulo, autor, ano)
        )
        conexao.commit()
        if cursor.rowcount > 0:
            print("Livro adicionado com sucesso")
        else:
            print("O livro não pode ser adicionado")

    except Exception as erro:
        print(f"erro ao tentar adicionar um livro {erro}")
    finally:
        if conexao:
            conexao.close()