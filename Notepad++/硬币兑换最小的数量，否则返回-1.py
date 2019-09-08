def func(prices, budget):
    prices.sort()
    dp = [float('inf')] * (budget + 1)
    dp[0] = 0
    for price in prices:
        for j in range(price, budget + 1):
            dp[j] = min(dp[j], dp[j - price] + 1)
    print(dp)
    return dp[-1] if dp[-1] != float('inf') else -1

prices = [100, 50, 30, 25]
budget = 155

print(func(prices, budget))

