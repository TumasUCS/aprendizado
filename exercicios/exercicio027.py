n = str(input('digite seu nome: ')).strip()
print('nome completo: {}'.format(n.title()))
print('primeiro nome: {}'.format(n.split()[0]))
print('ultimo nome: {}'.format(n.split()[-1]))
