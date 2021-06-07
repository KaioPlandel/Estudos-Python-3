#mostre quantas milhar centena dezena e unidade tem o numero digitado
num = input('Digite um numero ate 9999: ')

if len(num) == 4:
    print(f'A milhar é {num[0]}')
    print(f'A Centena é {num[-3]}')
    print(f'A Dezena é {num[-2]}')
    print(f'Unidade é {num[-1]}')
elif len(num) == 3:
    print(f'A Centena é {num[-3]}')
    print(f'A Dezena é {num[-2]}')
    print(f'Unidade é {num[-1]}')
elif len(num) == 2:
    print(f'A Dezena é {num[-2]}')
    print(f'Unidade é {num[-1]}')
else:
    print(f'Unidade é {num[-1]}')

