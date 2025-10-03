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
        titulo = input("Digite o nome do livro: ")
        autor = input("Digite o nome do autor: ")
        ano = int(input("Digite o ano que o livro foi lançado: "))
        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano)
        VALUES (?, ?, ?, ?)
        """,
        (titulo, autor, ano, "sim")
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

def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"ID {linha[0]} | TÍTULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIBILIDADE {linha[4]}")
    except Exception as erro:
        print(f"Erro ao tentar listar os livros{erro}")
    finally:
        if conexao:
            conexao.close()

def atualizar_disponibilidade():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    try:
        id = int(input("Digite o ID do livro que deseja ver: "))
    except ValueError:
        print("erro ao procurar o ID do livro")
        return

    try:
        cursor.execute("""
        UPDATE livros
        SET disponivel = CASE disponivel
        WHEN "sim" THEN "não"
        WHEN "não" THEN "sim"
        Else "sim"
        END 
        WHERE id = ?
       """,
       (id,)
       )
        conexao.commit()
    except Exception as erro:
        print(f"Ocorreu um erro ao atualizar o livro {erro}")
    finally:
        if conexao:
            conexao.close()

def remover_livro(id_livro):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros WHERE ID = ?", (id_livro,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("o Livro foi removido com sucesso")
        else:
            ("Nenhum livro foi encontrado com o ID fornecido.")
    except Exception as erro:
        print(f"erro ao tentar remover livro {erro}")
    finally:
        if conexao:
            conexao.close()

remover = int(input("Digite o ID do livro que deseja remover: "))


print("*"* 40)
print("Menu - Biblioteca")
print("*"* 40)
print("1 - Cadastrar livro")
print("2 - Listar livros")
print("3 - Atualizar disponibilidade")
print("4 - Remover livro")
print("5 - Sair")
opcao = int(input("Escola uma opção: "))
while True:
    if opcao == 1:
        adicionar_livro()
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        atualizar_disponibilidade()
    elif opcao == 4:
        remover_livro()
    elif opcao == 5:
        print("Saindo do sistema. . .")
        break