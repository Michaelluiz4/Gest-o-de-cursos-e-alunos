from db import conectar

def inserir_cursos():
    conn, cursor = conectar()

    nome_curso = input("Nome do curso: ")
    try:
        carga_horaria = int(input("Carga horária do curso: "))
        nivel = input("Nível do curso (Básico, Intermediário, Avançado): ")
        nivel = nivel.lower().replace("á", "a").replace("ç", "c")

        if nivel in ["basico", "intermediario", "avancado"]:
            cursor.execute("""
                              INSERT INTO cursos (nome, carga_horaria, nivel)
                              VALUES (?, ?, ?)
                              """, (nome_curso, carga_horaria, nivel))
        else:
            print("Nível incorreto. ")
    except ValueError:
        print("Carga horária invalída. ")

    conn.commit()
    conn.close()
