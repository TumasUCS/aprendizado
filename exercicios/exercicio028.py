import random
from time import sleep
while True:
    n = int(input('digite um numero: '))
    nr = random.randint(1, 5)
    print('processando...')
    sleep(3)
    if n == nr:
        print('o numero esta correto')
        break
    else:
        print('=' * 31)
        print(f'o numero era {nr}, tente novamente')
        print('=' * 31)