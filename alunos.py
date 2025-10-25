from db import conectar

def listar_cursos():
    try:
        conn, cursor = conectar()

        cursor.execute("SELECT id, nome FROM cursos")
        for curso in cursor.fetchall():
            print(f"{curso[0]} - {curso[1]}")

        conn.close()
    except Exception as e:
        print("\033[31mERRO.\033[0m Não foi possível conectar com o banco de dados. ", e)


def inserir_alunos():
    listar_cursos()

    nome = input("Nome do aluno: ").capitalize()

    try:
        conn, cursor = conectar()

        idade = int(input("Idade: "))
        curso_id = int(input("ID do curso: "))

        cursor.execute("SELECT id FROM cursos WHERE id = ?", (curso_id,))
        if cursor.fetchone():
            cursor.execute("""
                           INSERT INTO alunos (nome, idade, curso_id)
                           VALUES (?, ?, ?)
                           """, (nome, idade, curso_id))
            conn.commit()

            print("\033[32mDados inseridos com sucesso.\033[0m")

            conn.close()
        else:
            print("\033[31mID do curso inválido.\33[0m") 
    except ValueError:
        print("\033[31mERRO.\033[0m Idade incorreta.")
    except Exception as e:
        print("\033[31mERRO.\033[0m Não foi possível inserir o aluno. ", e)
