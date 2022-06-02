lista_de_cadastro = []
opcao = 1

print('CONTROLE DE FUNCIONÁRIOS')

while opcao != 0:

    print('''O que você deseja fazer?\n
    1 - Incluir funcionário.
    2 - Alterar funcionário.
    3 - Listar funcionários.
    4 - Remover funcionário.
    5 - Aumento de salário.
    6 - Sair!''')

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        print('INCLUSÃO DE FUNCIONÁRIO:')

        pessoa = []

        codigo = input('Código do funcionário: ')
        pessoa.append(codigo)

        nome = input('Nome do funcionário: ')
        pessoa.append(nome)

        email = input('E-mail:')
        pessoa.append(email)

        datainicio = str(input('Digite a data de admissão (00/00/00)'))
        pessoa.append(datainicio)

        salario = float(input('Salário do funcionário em R$: '))
        pessoa.append(salario)

        lista_de_cadastro.append(pessoa)

        print('Funcionário Cadastrado')

    if opcao == 2:
        print('ALTERAÇÃO DE FUNCIONÁRIO')

    if opcao == 3:

        if lista_de_cadastro == []:
            print('Nenhum funcionário cadastrado!')

        else:
            print('LISTAGEM DE FUNCIONÁRIOS \n')
            for funcionario in lista_de_cadastro:
                print(lista_de_cadastro, end=', ')

    if opcao == 4:
        print('DESLIGAMENTO DE FUNCIONÁRIO')
        removerfunc = input('Digite o código do funcionário: ')
        lista_de_cadastro.pop(removerfunc)
        print('Funcionário removido')

    if opcao == 5:
        print('ALTERAÇÃO DE SALÁRIO')

    elif opcao == 6:
        print('Programa encerrado!')
        break

    else:
        print('Insira apenas os números do MENU.')
