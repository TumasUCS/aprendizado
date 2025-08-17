n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n3 = int(input('digite mais um numero: '))
if n1 > n2 and n1 > n3:
    print(f'o maior numero digitado foi {n1}')
elif n2 > n1 and n2 > n3:
    print(f'o maior numero digitado foi {n2}')
elif n3 > n1 and n3 > n2:
    print(f'o maior numero digitado foi {n3}')
if n1 < n2 and n1 < n3:
    print(f'e o menor numero foi {n1}')
elif n2 < n1 and n2 < n3:
    print(f'e o menor numero foi {n2}')
elif n3 < n1 and n3 < n2:
    print(f'e o menor numero foi {n3}')