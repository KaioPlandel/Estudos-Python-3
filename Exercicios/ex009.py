#faça uma função que pegue um numero positivo e trasforma em negativo
def make_negative(number):
    if number > 0:
        return number * -1
    elif number == 0:
        return 0
    else:
        return number


print(make_negative(1))