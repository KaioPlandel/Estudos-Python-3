# sorteia o nome de 4 alunos para apagar o quadro
from random import randint
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('NOme do aluno 3: ')
a4 = input('Nome do aluno 4: ')
lista = [a1,a2,a3,a4]
sorteio = randint(0,3)
print(f'O aluno sorteado foi {lista[sorteio]}')

