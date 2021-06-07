
n = int(input('Escreva um Numero Qualquer: '))
print(f'O Numero digitado foi {n}')

print('=-'*30)
print('''Converter para OCTAL:       [1]
Converter para BINÁRIO:     [2]
Converter para HEXADECIMAL: [3]''')

resp = int(input('Digite a Opção Adequada Para oque você deseja: '))

if resp == 1:
    print(f'O numero convertido para OCTAL é {oct(n)}')
elif resp == 2:
    print(f'O numero convertido para BINÁRIO é {bin(n)}')
elif resp == 3:
    print(f'O numero convertido para HEXADECIMAL é {hex(n)}')
print('=-'*30)
