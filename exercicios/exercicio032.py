ano = int(input('digite o ano: '))
if ano % 4 == 0 and ano < 2025:
    print(f'{ano} foi bissexto')
elif ano % 4 == 0 and ano >= 2025:
    print(f'{ano} vai ser bissexto')
elif ano % 4 != 0 and ano >= 2026:
    print(f'{ano} nao vai ser bissexto')
else:
    print(f'{ano} nao foi bissexto')