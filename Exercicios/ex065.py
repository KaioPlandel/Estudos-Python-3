resp = 'S'
cont = 0
soma = 0
while resp != 'N':
    if resp not in 'SN':
        print('Informação Invalida')
        resp = str(input('Deseja Continuar S/N: ')).upper().strip()[0]
    else:
        print('~-'*30)
        n = int(input('Digite um valor: '))
        cont += 1
        soma += n
        resp = str(input('Deseja Continuar S/N: ')).upper().strip()[0]
        print('~-' * 30)
print(f'Foram digitados {cont} Numeros\n A media digitada é {soma/cont:.1f}')
