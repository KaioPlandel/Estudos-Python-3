def neg(list):
    for c in list:
        if c < 0:
            print(c)

a = [1,2,3]

b = a
print(b)
a = 3
print(b)
print(a)