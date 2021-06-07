from time import sleep
s = 1
while s == 1:
    print('-' * 30)
    print('      Caixa Eletronico')
    print('-' * 30)
    valor = int(input('Quanto Deseja Sacar: '))
    if valor > 600:
        print('Digite um Valor Até R$ 600,00')
    else:
        print(f'TOTAL SAQUE: R${valor}')
        cont100 = 0
        cont50 = 0
        cont10 = 0
        cont5 = 0
        cont1 = 0
        while valor != 0:
            if valor >= 100:
                valor -= 100
                cont100 +=1
            elif valor >= 50:
                valor -= 50
                cont50 += 1
            elif valor >= 10:
                valor -= 10
                cont10 += 1
            elif valor >= 5:
                valor -= 5
                cont5 += 1
            elif valor >= 1:
                valor -= 1
                cont1 += 1
        s = 0
        if cont100 >= 1:
            print(f'Foram {cont100} Notas de R$100,00')
        if cont50 >= 1:
            print(f'Foram {cont50} Notas de R$ 50,00')
        if cont10 >=1:
            print(f'Foram {cont10} Notas de R$ 10,00')
        if cont5 >= 1:
            print(f'Foram {cont5} Notas de R$ 5,00')
        if cont1 >= 1:
            print(f'Foram {cont1} Notas de R$ 1,00')
        print('-' * 30)
    resp = input('Deseja Fazer mais um Saque S/N:  ').strip().upper()[0]
    if resp == 'S':
        sleep(1)
        s = 1
    else:
        print('-' * 30)
        print('Obrigado Volte Sempre!!')
        print('-' * 30)

