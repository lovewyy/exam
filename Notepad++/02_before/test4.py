"""
​输入1 2 3 4 5
​输出 ture
​"""
import sys
a = sys.stdin.readline().split()
l = []
t = {'1': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
for i in a:
    if i in t.keys():
        l.append(t[i])
    else:
        l.append(0)

print(a)
print(l)

if len(l) != 5:
    print('输入错误')
else:
    if len(l) < 1:
        print('false')
    else:
        t = {}
        for i in l:
            if i == 0:
                continue
            if i in t.keys():
                print('false')
            else:
                t[i] = 1

    print(t)
    print(max(t.keys()))

    if int(max(t.keys())) - int(min(t.keys())) <= 4:
        print('true')
    else:
        print('false')