# 8开头，11位数 怎么通过n次删除得到

# 偶数个数两两配对，配对和最小 1个8 1个2 2个5 得10

# 第三题：把 一个 分成 两个 长度相差不超过1的 和相差最小的数组


# 第四题：排序 3 5 6 8 8 10 10 每一轮减里面非负数最小的
import sys
line = sys.stdin.readline().strip()
va = list(map(int, line.split()))
n = va[1]
line = sys.stdin.readline().strip()
va = list(map(int, line.split()))
va = list(set(va))
va.sort()
va = [0] + va
lenva = len(va)
temp = 0
for i in range(min(n, lenva - 1)):
    print(va[i + 1] - va[i])

