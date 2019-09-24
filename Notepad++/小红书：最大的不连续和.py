import sys

n = int(sys.stdin.readline().strip())

line = sys.stdin.readline().strip()

a = list(map(int, line.split()))

a = [None] + a

print(a)

dp = [ [ [0 for i in range(2)] for j in range(n+1)] for k in range(n+1)]

dp[1][1][1] = a[1]

for i in range(2, n+1):
    dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1])
    dp[i][1][1] = max(dp[i-1][0][0], dp[i-2][0][0]) + a[i]

for i in range(2, n+1):
    for j in range(2, (i + 1) // 2 + 1):
        dp[i][j][0] = max(dp[i-1][j][1], dp[i-1][j][0])
        dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-2][j-1][0], dp[i-2][j-1][1]) + a[i]

ans = 0
have = 0

for i in range((n+1) // 2, -1, -1):
    for j in range(0, 2):
        if dp[n][i][j] >= have:
            ans = i
            have = dp[n][i][j]

print(have, ans)