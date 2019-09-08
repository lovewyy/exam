import sys

def maxsub(nums):
    maxsub = nums[0]
    st = 0
    en = 0
    for i in range(len(nums)):
        j = i
        for j in range(len(nums)):
            s = 0
            k = j
            for k in range(i,j+1):
                s += nums[k]
            if s < minsub:
                minsub = s
                st = i
                en = j
    for i in range(st, en+1):
        if nums[i] > 0:
            pass
    return minsub

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    print(minsub(a))
