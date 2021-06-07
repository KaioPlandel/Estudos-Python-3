from random import  randint
from time import sleep
jogo = ['PEDRA','PAPEL','TESOURA']
pc = randint(1,3)
print('-='*30)
print('                    VAMOS JOGAR JOKENPOW')
print('-='*30)
jogador = int(input('Digite O numero correspondente a sua Jogada: \n\n'
                    'PEDRA =   [1]\n'
                    'PAPEL =   [2]\n'
                    'TESOURA = [3]\n \n'
                    'OPÇÃO: '))
print('JOO')
sleep(1)
print('KEEN')
sleep(1)
print('POOW')
sleep(2)
print(f'VOCÊ JOGOU {jogo[jogador-1]} E EU JOGUEI {jogo[pc-1]}')
if jogador == 1:
    if pc == 1:
        print('EMPATOU!!')
    elif pc == 2:
        print('VOCÊ PERDEU HAHAHA!!')
    elif pc == 3:
        print('VOCÊ GANHOU!!')
elif jogador == 2:
    if pc == 2:
        print('EMPATOU!!')
    elif pc == 3:
        print('VOCÊ PERDEU HAHAHA!!')
    elif pc == 1:
        print('VOCÊ GANHOU!!')
elif jogador == 3:
    if pc == 3:
        print('EMPATOU!!')
    elif pc == 1:
        print('VOCÊ PERDEU HAHAHA!!')
    elif pc == 2:
        print('VOCÊ GANHOU!!')
else:
    print('OPÇÃO INVALIDA!')