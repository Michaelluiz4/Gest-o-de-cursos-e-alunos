import db
from cursos import inserir_cursos
from alunos import inserir_alunos

def menu():

    while True:
        print("-=" * 20)
        print("Escolha a opção desejada")
        print("[1] - Inserir curso")
        print("[2] - Inserir aluno")
        print("[0] - Sair")

        try:
            opcao = int(input("Escolha: "))
            print("-=" * 20)

            if opcao == 1:
                inserir_cursos()
            elif opcao == 2:
                inserir_alunos()
            elif opcao == 0:
                break
        except ValueError:
            print("\033[31mERRO.\033[0m Opção inválida.")

    
if __name__ == "__main__":
    db.criar_tabelas()
    menu()