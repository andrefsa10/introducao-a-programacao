nome = 'andré'  # str
idade = 25  # int
altura = 1.75  # float
e_maior = idade > 18  # bool
peso = 82
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0}{1}{0} tem {2}{1} anos e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {id} anos e seu imc é {im}'.format(n=nome, id=idade, im=imc))
