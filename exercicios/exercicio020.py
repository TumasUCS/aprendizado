import random
aluno1 = str(input('nome do aluno: '))
aluno2 = str(input('nome do aluno: '))
aluno3 = str(input('nome do aluno: '))
aluno4 = str(input('nome do aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('o aluno escolhido foi: {}'.format(lista))
