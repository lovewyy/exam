# 阅文：array中奇数放左边偶数放右边
def adj(a, s):
    j = -1
    for i in range(s):
        if a[i] % 2 == 1:
            j += 1
            a[i], a[j] = a[j], a[i]

a = [2,3,4,3,54,54,423,23,2]
adj(a, 9)
print(a)

# 阅文：序列中连续最大的数，并返回此子数组
def func(a, N, start, end):
    maxSum = 0
    thisSum = 0
    i = 0
    start = 0
    end = 0
    for i in range(0, N):
        thisSum += a[i]
        if thisSum > maxSum:
            maxSum = thisSum
            end = i
        if thisSum < 0:
            thisSum = +0
            if i < N - 2 and a[i + 1] > 0:
                start = i + 1

    if start == 0 and end == 0 and a[0] <= 0:
        start = -1
        end = -1
    return maxSum, a[start:end + 1]

print(func([-1, 2, -1, 3, 4, 5], 6, 0, 0))

# 搜狗：第一题：IP过滤，第二题：密码