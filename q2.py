def cadastro_de_alunos ():
    alunos = []
    opcao = 0

    print("Cadastro de Alunos: ")
    while not opcao == 3:
        print("(1) Cadastrar (2) Listar (3) Sair")
        opcao = int(input("Digite a opção desejada:  "))

        if opcao == 1:
            matricula = int(input("Digite a matricula do aluno: "))
            nota1 = float(input("Digite a nota1:  "))
            nota2 = float(input("Digite a nota2:  "))
            nota3 = float(input("Digite a nota3:  "))
            aluno = {
                "matricula": matricula,
                "notas":  [
                    nota1,
                    nota2,
                    nota3
                ]
            }
            alunos.append(aluno)
        elif opcao == 2:
            for aluno in alunos:
                print(aluno)

    print("Finalizado.")




if __name__ == "__main__":
  cadastro_de_alunos()

