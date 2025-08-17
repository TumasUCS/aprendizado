frase = str(input(('digite uma frase: '))).strip().lower()
print ('a frase contem {} letras a'.format(frase.count('a')))
print ('a primeira letra a aparece na posição {}'.format(frase.find('a')+1))
print ('a ultima letra a aparece na posição {}'.format(frase.rfind('a')+1))