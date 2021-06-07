from time import sleep
n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite Outro Numero: '))
resp = 0
while resp != 5:
    print('=-' * 30)
    sleep(1)
    resp = int(input('''ESCOLHA A OPÇÃO DESEJADA:
    [1] = SOMAR
    [2] = MULTIPLICAR
    [3] = MAIOR NUMERO
    [4] = NOVOS NUMEROS
    [5] = SAIR DO PROGRAMA
    RESPOSTA: '''))
    print('=-'*30)
    if resp == 1:
        sleep(0.5)
        print(n1+n2)
    elif resp == 2:
        sleep(0.5)
        print(n1*n2)
    elif resp == 3:
        sleep(0.5)
        print(max(n1,n2))
    elif resp == 4:
        sleep(0.5)
        n1 = int(input('Digite um Numero: '))
        n2 = int(input('Digite Outro Numero: '))
    elif resp == 5:
        sleep(0.5)
        print('Saindo do programa')
    else:
        sleep(0.5)
        print('OPÇÃO INVALIDA')