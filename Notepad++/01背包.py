# 01背包
def bags(weight, value, t):
    dp = [ [0 for j in range(t+1)] for i in range(len(weight)+1)]
    for i in range(1, len(weight)+1):
        for j in range(t+1):
            if j < weight[i-1]: 
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + value[i-1])
    return dp[-1][-1], dp[-1]

# 更优解
def bags2(w, v, c):
    dp = [ 0 for _ in range(c + 1)]
    for i in range(len(v)):
            for j in range(c, w[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[-1], dp

# 完全背包
def cBags(w, v, c):
    dp = [0 for _ in range(c + 1)]
    for i in range(len(v)):
            for j in range(w[i], c + 1):
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[-1], dp

def dBags(w, v, n, c):
    dp = [0 for _ in range(c + 1)]
    for i in range(len(v)):
        for k in range(n[i]):
            for j in range(c, w[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[-1], dp

def dBags2(w, v, n, c):
    dp = [0 for _ in range(c + 1)]
    for i in range(len(v)):
        for j in range(c, -1, -1):
            for k in range(n[i] + 1):
                if j - k * w[i] < 0:
                    break
                dp[j] = max(dp[j], dp[j - k * w[i]] + k * v[i])
    return dp[-1], dp

# 测试
weight=[5, 4, 7, 2, 6]
value =[12,3,10, 3, 6]
nums = [2, 3, 2, 3, 2]
t = 15
print(bags(weight, value, t))
print(bags2(weight, value, t))
print(cBags(weight, value, t))
print(dBags(weight, value, nums, t))
print(dBags2(weight, value, nums, t))



