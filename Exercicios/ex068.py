#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import  randint
print('~~'*25)
print('              JOGO DE PAR OU IMPAR')
print('~~'*25)
vitoria = 0
while True:
    pc = randint(0,10)
    num = int(input('Digite um Numero: '))
    opcao = str(input('Você Quer P/I: ')).upper().strip()[0]
    if opcao not in 'PI':
        print('Digite Uma Opção Válida: ')
    else:
        resultado = pc + num
        if resultado % 2 == 0:
            res = 'PAR'
            print(f'Você Jogou {num} e o Computador {pc} Deu PAR')
            print('~~' * 25)
        else:
            res = 'IMPAR'
            print(f'Você Jogou {num} e o Computador {pc} Deu IMPAR')
            print('~~' * 25)
        if opcao == 'P' and res == 'PAR':
            vitoria += 1
            print('Você Ganhou!')
        elif opcao == 'I' and res == 'IMPAR':
            vitoria += 1
            print('Você Ganhou!')
        else:
            print('Você Perdeu!')
            break
print(f'Você teve {vitoria} Vitórias Consecutivas.')
