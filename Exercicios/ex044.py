# digite o preço do produto e defina descontos de acordo com a forma de pagamento
from time import sleep
preco = float(input('Digite o Preço do Produto: '))
print('=-'*30)
formaPG = int(input('Digite o Numero Correspondente a Forma de Pagamento\n'
                    'A Vista Dinheiro Ou Cheque: [1]\n'
                    'A Vista No Cartão:          [2]\n'
                    '2x No Cartão:               [3]\n'
                    '3x ou Mais:                 [4]\n'
                    'OPÇÃO:  '))
print('=-'*30)
sleep(2)
print(f'O Valor do Produto é R${preco:.2f}')
if formaPG == 1:
    desconto = preco * 0.10
    print(f'O Total a pagar com o Desconto de 10% é R${preco-desconto:.2f}')
elif formaPG == 2:
    desconto = preco * 0.05
    print(f'O Valor a pagar com 5% de Desconto é R${preco - desconto:.2f}')
elif formaPG == 3:
    print(f'O Valor Total a Pagar é R${preco:.2f}')
elif formaPG == 4:
    vezes = int(input('Quantas vezes Pretende Parcelar: '))
    juros = preco *0.20
    print(f'Sera Parcelado em {vezes}x no Valor de {(preco + juros) / vezes:.2f} ')
    print(f'O Total Sera R${preco+juros:.2f}')
sleep(2)
print(f'Obrigado Pela Compra!!')