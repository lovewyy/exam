def coinChange(coins, amount):
	coins.sort() 
	dp = {0:0} 
	for i in range(1,amount + 1):
		dp[i] = amount + 1 
		for j in range(1, amount):
			dp[i]=min(dp[i],dp[i-j]+1)
	if dp[amount] == amount + 1: 
		return -1
	else:
		return dp[amount]



print(coinChange([1,2,5,10], 19))

# a = 0
# for i in range(1,21):
    # if coinChange([1, 2, 5, 10], i) > a:
        # a = coinChange([1, 2, 5, 10], i)
    # elif coinChange([1, 2, 5, 10], i) == -1:
        # a = -1
        # break
# print(a)