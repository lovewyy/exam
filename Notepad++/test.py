import sys

def func(a):
    suma = sum(a)
    dp = [ [ 0 for _ in range(suma // 2 + 1)] for _ in range(len(a) + 1)]
    
    for i in range(1, len(a) + 1):
        for j in range(suma // 2 + 1):
            if j >= a[i - 1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - a[i - 1]] + a[i -1])
            else:
                dp[i][j] = dp[i - 1][j]
    return suma - 2 * dp[-1][-1]

a = [1, 56, 23, 34, 23, 112, 200, 30, 50, 60, 503, 199]

print(func(a))
