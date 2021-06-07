listaNomes = []
for c in range(0,5):
    nome = input('Digite um nome: ').upper()
    listaNomes.append(nome)

for i in listaNomes:
    if i[0] in 'ABCDEFGHIJKLM':
        print(i)

