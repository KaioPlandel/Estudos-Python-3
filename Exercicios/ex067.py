#Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:
    print('~~' * 22)
    tabuada = int(input('Digite o numero para ver sua Tabuada: '))
    if tabuada >= 0:
        print(f'Tabuada do numero {tabuada}')
        for c in range(1,11):
            print(f'{tabuada} x {c} = {tabuada * c}')
    else:
        print('Saindo do Programa...')
        break
print('Programa Finalizado!')
