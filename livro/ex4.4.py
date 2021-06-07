#Escreva a função par() que toma um inteiro positivo n como entrada e
# exibe na tela todos os números entre 2 (inclusive) e n, que sejam divisíveis por 2 ou por 3,
# usando este formato de saída:

def par(n):
    for c in range(2,n):
        if c % 2 == 0 or c % 3 == 0:
            print(f'{c}',end=',')

par(17)