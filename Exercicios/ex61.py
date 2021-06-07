primeiro = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a razão: '))
c = 0
termos = 10
while c < termos:
    print(primeiro)
    primeiro += razao
    c += 1
    if c == termos:
        termos = int(input('Quantos tempos deseja mostrar Mais: '))
        c = 0
print('PROGRAMA ENCERRADO')
