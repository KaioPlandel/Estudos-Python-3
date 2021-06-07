#Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.

"""idade = eval(input('Digite sua idade: '))
if idade > 62:
    print('Você pode se aposentar')"""

#Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
# exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.

lista = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
nome = input('Digite o Nome: ')
if nome in lista:
    print('Kaio Bonitão')

#Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…

golpe = eval(input('Digite o valor do Golpe: '))
defesa = eval(input('Digite o Valor da Defesa: '))

if golpe > defesa:
    print('Você esta morto')

# Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'

