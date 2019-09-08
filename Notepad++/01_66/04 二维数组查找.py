# 4: in array find target

# reverse
test = [1, 2, 3, 4, 5]
for i in reversed(test):
    print(i, end = ' ')
print()
for i in test[::-1]:
    print(i, end = ' ')
print()
for i in range(len(test)-1, -1, -1):
    print(test[i], end = ' ')
print()

print(list(reversed(test))) # function
test.reverse()              # class.funciton
print(test)

# 源码


