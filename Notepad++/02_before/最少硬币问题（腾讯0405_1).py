class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res = array[0]
        sum = res
        p = 0
        count = 0
        for i in range(1,len(array)):
            if sum < 0: 
                sum = sum + array[i]
            else:
                sum = array[i]
            if sum < res:
                res = sum
                p = i

        return res, p, count

s = Solution()
print(s.FindGreatestSumOfSubArray([2, -2, 7, 6, -8, -10, -5, 2, -13, -45, -23, 5, -34, 4, -4]))