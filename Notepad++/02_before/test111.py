def finds(nums, t):
    count = 0
    for a in range(0, nums[0] + 1):
        for b in range(0, nums[1] + 1):
            for c in range(0, nums[2] + 1):
                for d in range(0, nums[3] + 1):
                    if a + 5*b + 10*c + 20*d == t:
                        count += 1
                        print(a,b,c,d)
    return count

nums = [5, 3, 2, 1]
t = 55
a = finds(nums, t)
print(a)

def finds2(nums, t):
    a = [1, 5, 10, 20]
    dp = [0 for j in range(t+1)]
    for i in range(4):
        for j in range(0, t+1):
            for k in range(0, nums[i]):
                if j > k*a[i]:
                    dp[j] += dp[j-k*a[i]]
    return dp[t]
print(finds2(nums, t))
