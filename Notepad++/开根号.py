def func(num):
    x = num 
    y = 0
    while abs(x - y) > 0.00001:
        y = x 
        x = (x + num / x) / 2
        print(y)
    return x 

print(func(2))
print("1.4142135623731")