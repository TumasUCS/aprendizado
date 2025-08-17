from random import choice
aluno1 = str(input('digite um nome: '))
aluno2 = str(input('digite um nome: '))
aluno3 = str(input('digite um nome: '))
aluno4 = str(input('digite um nome: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolha = choice(lista)
print('o aluno escolhido foi {}'.format(escolha))