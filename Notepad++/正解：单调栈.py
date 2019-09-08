# 单调栈

n = 5
a = [7,2,4,6,5,-1]

st = []
sumL = []
sumV = 0
sumL.append(0)
for i in range(1, n+2):
    sumV += a[i-1]
    sumL.append(sumV)
res = 0
for i in range(n+1):
    if len(st) == 0 or a[i] >= st[-1]:
        st.append(a[i])
    else:
        while len(st)!= 0 and a[i] < st[-1]:
            index = len(st)
            top = st.pop(-1)
            temp = sumL[i] - sumL[index]
            if temp * top > res:
                res = temp * top
        st.append(a[i])
print(res)