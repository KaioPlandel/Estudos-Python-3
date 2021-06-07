# Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings)
# e depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista

palavras = input('Digite uma lista de palavras:')

nome = palavras.strip().split()

for c in nome:
    if len(c) == 4:
        print(c)


