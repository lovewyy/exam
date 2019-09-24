n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
m = 3
n = 3
def func(n1, m, n2, n):
    s = m + n 
    m -= 1
    n -= 1
    while n >= 0:
        s -= 1
        if m >= 0 and n1[m] > n2[n]:
            n1[s] = n1[m]
            m -= 1
        else:
            n1[s] = n2[n]
            n -= 1
func(n1, 3, n2, 3)
print(n1)


def isHappy(d):
    return isHappy(sum(int(i) ** 2 for i in str(d))) if d > 4 else d == 1 
print(isHappy(32))


prices = [1, 3, 2, 8, 4, 9]
fee = 2
def func(prices, fee):
    total = 0
    now = -float('inf')
    for i in range(len(prices)):
        temp = total
        total = max(total, now + prices[i])
        now = max(now, temp - prices[i] - fee)
    return total
print(func(prices, fee))


def func1(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    res = 0
    while i <= j:
        res += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return res
people = [3,2,2,1]
limit = 3
print(func1(people, limit))