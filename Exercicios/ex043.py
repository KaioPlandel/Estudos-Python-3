#calculo IMC
peso = float(input('Digite o Peso: '))
altura = float(input('Digite a Altura: '))

imc = peso / (altura **2)

if imc < 1.85:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBITA')