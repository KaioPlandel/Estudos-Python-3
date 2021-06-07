def pagar(Shora,horas):
    if horas <= 40:
        total = Shora * horas
        print(f'O Valor a Pagar é R${total}')
    else:
        totalHr = (horas - 40) * 15
        total = (Shora * 40) + totalHr
        print(f'O Valor a Pagar com o aumento é R${total}')

pagar(10,45)