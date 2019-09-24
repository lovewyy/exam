#
'''
Welcome to vivo !
'''

def solution(N,M):
    
    # TODO Write your code here
    dp = [i for i in range(1, N + 1)]
    dp2 = []
    i = 0
    while len(dp) != 1:
        ldp = len(dp)
        flag = []
        for j in range(ldp):
            i += 1
            if i % M == 0:
                dp2.append(dp[j])
                flag.append(j)
        flag2 = 0
        for k in flag:
            kk = k - flag2
            dp.pop(kk)
            flag2 += 1

    dp2.append(dp[0])
    return dp2

N,M = [int(i) for i in input().split()]
print(solution(N,M))