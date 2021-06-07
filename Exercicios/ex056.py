somaID = 0
velho = 0
idF = 0
for c in range(0,4):
    nome = str(input('Digite o Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper().strip()[0]
    somaID += idade
    if sexo == 'M':
        if idade > velho:
            no = nome
            velho = idade
    if sexo == 'F' and idade < 20:
        idF += 1

print(f'A Media de idade de todos é {somaID/4}')
print(f'O Homem mais Velho é o {no} com {velho} anos')
print(f'Existe {idF} Mulheres menores de 20')

