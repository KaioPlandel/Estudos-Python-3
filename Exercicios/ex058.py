from random import  randint
from time import sleep
print('-='*30)
print('                   JOGO DA ADIVINHAÇÃO\n')
print('      TENTE ADIVINHAR O NUMERO QUE EU PENSEI ENTRE 0 E 5')
print('-='*30)
n = 0
pc = -1
palpites = 0
while pc != n:
    pc = randint(0, 3)
    n = int(input('Digite o Numero: '))
    while n > 3:
        print('NUMERO INVALIDO, TEM QUE SER ENTRE 0 E 5')
        n = int(input('Digite o Numero: '))
    sleep(1)
    print(f'Você digitou {n} e eu pensei em {pc}\n')
    palpites += 1
    if pc == n:
        print('ACERTOU')
    else:
        print('ERROU')

print('-='*30)
print('CONSEGUIU ISSO AI..')
print(f'Você teve {palpites} Palpites até Acertar')
print('-='*30)