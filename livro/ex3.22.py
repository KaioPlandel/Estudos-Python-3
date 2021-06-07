#3.22 Implemente um programa que solicita uma lista de palavras do usuário
# e depois exibe cada palavra na lista que não seja 'segredo'.

lista = eval(input('Digite uma lista: '))
for c in lista:
    if c != 'segredo':
        print(c)