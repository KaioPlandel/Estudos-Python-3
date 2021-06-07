# Se o ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'

ano = eval(input('Digite o Ano: '))

if ano % 4 == 0:
    print('Pode ser Um ano Bissexto')
else:
    print('Definitivamente não é Um ano Bissexto')

# Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez

bilhete = eval(input('Digite 4 numeros: '))
loteria = [1,2,4,3]
print(bilhete)
if bilhete == loteria:
    print('Voce Ganhou')
else:
    print('Não foi desta Vez')