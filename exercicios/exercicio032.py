from datetime import date
ano = int(input('digite o ano que voce quer analisar e digite 0 para analisar o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 and ano < 2025:
    print(f'{ano} foi bissexto')
elif ano % 4 == 0 and ano >= 2025:
    print(f'{ano} vai ser bissexto')
elif ano % 4 != 0 and ano >= 2026:
    print(f'{ano} nao vai ser bissexto')
else:
    print(f'{ano} nao foi bissexto')
    
