#mostre quando a pessoa vai pagar com o desconto de 5%
preco = float(input('Digite o Preço do Produto R$: '))
desconto = preco * 0.05
print(f'O preço do Produto é de R${preco:.2f} com o Desconto de R${desconto:.2f} \nO Total vai ficar R$:{preco - desconto:.2f}')