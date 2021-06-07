n = int(input('Digite um numero Qualquer: '))
c = n
f = 1
d = 0
while c > 0:
    c -= 1
    d += 1
    f *= d
    print(f'{c+1}->',end=' ')
print(end='= ')
print(f)