# 分成两组相差最小的组

# 数量不等，相差最小
def func(list1):
    one_list = list(list1)
    one_list.sort()
    two_list = []
    n = len(one_list)
    total = sum(one_list)
    half_total = total / 2
    s = 0
    for i in range(n-1, -1, -1):
        ns = s + one_list[i]
        if ns > half_total:
            continue
        else:
            s += one_list[i]
            two_list.append(one_list[i])
            one_list.pop(i)
            if abs(s - half_total) < one_list[0]:
                break
    a = sum(one_list)
    b = sum(two_list)
    return abs(a - b), one_list, two_list

a = [1, 56, 23, 34, 23, 112, 200, 30, 50, 60, 503, 199]
print(func(a))

print()

# ******************************************************
# vivo要求，数量相差最大为1，质量相差最小

n = len(a)
s = sum(a)
t = s // 2

f = [ [0 for _ in range(n * max(a) // 2 + max(a) + 1)] for _ in range(n // 2 + 2)]

f[0][0] = 1

mk = 0
mj = 0
for i in range(1, n + 1):
    for j in range(min(n // 2, i - 1), -1, -1):
        for k in range(0, j * max(a) + 1):
            if f[j][k]:
                f[j + 1][k + a[i - 1]] = 1     # i - 1 是第i个数
                

i = 0
while True:
    if f[n // 2][t + i]:
        print(min(t + i, s - t - i), max(t + i, s - t - i))
        # print(abs(2 * t + 2 * i - s))
        print(1)
        break
    if f[n // 2][t - i]:
        print(min(t + i, s - t + i), max(t + i, s - t + i))  
        # print(abs(2 * t - s))
        print(2)
        break
    i += 1

print(mj, mk)
