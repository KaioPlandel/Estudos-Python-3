sexo = str(input('Digite o Sexo: ')).upper().strip()[0]

while sexo not in 'MF':
    print('AVISO: SEXO INVALIDO')
    sexo = str(input('Digite o sexo: ')).strip().upper()[0]
