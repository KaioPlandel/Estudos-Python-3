import numpy
from random import randint

linhas = 5
notasAlunos = numpy.zeros(linhas)
print(notasAlunos)

index = 0
alunos = 5

while index < alunos:
    notasAlunos[index] = float(input(f'Digite a nota do aluno {index+1} [0/1]: '))
    if notasAlunos[index] < 0 or notasAlunos[index] > 1:
        print('ERRO')
    else:
        index += 1

print(notasAlunos)

