#crie um programa que mostre quantos metros quadrados a parede tem
#e quanto vai gastar para pinta-la considerando q 1 litro pinta 2 metros quadrados
altura = float(input('Digite a Altura: '))
largura = float(input('Largura: '))
parede = altura * largura
litro = parede / 2

print(f'O Tamanho da parede é de {parede}m \nÉ Necessário {litro} Litros para fazer a pintura')

