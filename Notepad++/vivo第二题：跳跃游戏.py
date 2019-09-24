'''
 Welcome to vivo !
'''

def solution(step_list):
    ll = len(step_list)
    if ll == 1:
        return 0
    dp = [(0, 0)]
    ans = [False] * ll
    while dp:
        a, b = dp.pop(0)
        for i in range(step_list[b], 0, -1):
            if b + i >= ll - 1:
                return a + 1
            if not ans[b + i]:
                dp.append((a + 1, b + i))
                ans[b + i] = True
    return -1

step_list = [int(i) for i in input().split()]
print(solution(step_list))