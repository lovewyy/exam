import sys
try:
    line = sys.stdin.readline().strip()
    v = list(map(int, line.split(',')))
    lv = len(v)
    ans = 1
    dp = [{} for _ in range(lv)]
    for i in range(1, lv):
        for j in range(i):
            c = v[i] - v[j]
            m = dp[j].get(c, 1)
            dp[i][c] = m + 1
        temp = max(dp[i].values())
        ans = max(ans, temp)
    print(ans)
except:
    print(0)