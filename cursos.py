from db import conectar

def inserir_cursos():

    nome_curso = input("Nome do curso: ")

    try:
        conn, cursor = conectar()

        carga_horaria = int(input("Carga horária do curso: "))
        nivel = input("Nível do curso (Básico, Intermediário, Avançado): ")
        nivel = nivel.lower().replace("á", "a").replace("ç", "c")

        if nivel in ["basico", "intermediario", "avancado"]:
            cursor.execute("""
                              INSERT INTO cursos (nome, carga_horaria, nivel)
                              VALUES (?, ?, ?)
                              """, (nome_curso, carga_horaria, nivel))
            conn.commit()

            print("\033[32mCurso cadastrado com sucesso.\033[0m")

            conn.close()
        else:
            print("\033[31mERRO.\033[0m Nível incorreto. ")
    except ValueError:
        print("\033[31mERRO.\033[0m Carga horária invalída. ")
    except Exception as e:
        print("\033[31mERRO.[0m Não foi possível inserir curso. ", e)
    
