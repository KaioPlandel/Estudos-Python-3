from random import  randint
print('-'*50)
print('TENTE ADIVINHAR O NUMERO QUE VOU PENSAR DE 0 A 5')
print('-'*50)
pc = randint(0,5)
numero = int(input('Digite o numero: '))
if numero > 5:
    print('NUMERO INVÁLIDO')
else:
    print(f'O COMPUTADOR JOGOU {pc} E VOCÊ JOGOU {numero}')
    if numero == pc:
        print('PARABÉNS VOCÊ ACERTOU')
    else:
        print('NÃO FOI DESSA VEZ')

