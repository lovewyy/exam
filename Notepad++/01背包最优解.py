# 01bags
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

weight=[5, 4, 7, 2, 6]
value =[12,3,10, 3, 6]
nums = [2, 3, 2, 3, 2]
t = 15
print(bags(weight, value, t))
print(bags2(weight, value, t))