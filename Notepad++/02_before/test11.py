import random

a = random.randint(0,1000)
lista = [i for i in range(1000)]
i = 0
while a not in lista:
    i += a
    print(i)

print(a)

