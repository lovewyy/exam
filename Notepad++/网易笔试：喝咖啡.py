#

k = 1
m = 15
test = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

k = 1
m = 7
test = [5, 9, 13, 17, 21, 25, 29]

k = 3
m = 3
test = [5, 10, 20]

if len(test) == 0:
    count = 30 // (k + 1)
    print(count)
else:
    w = []

    count = len(test)

    v = test[0]
    while v > 0:
        if v - k - 1 >= 1:
            w.append(v - k - 1)
            count += 1
        v -= k + 1

    # print(w + test)

    ww = []
    back = test[-1]
    while back < 30:
        if back + k + 1 <= 30:
            ww.append(back + k + 1)
            count += 1
        back += k + 1

    www = []
    for i in range(0, len(test) - 1):
        mid = test[i] + k + 1
        while mid + k + 1 <= test[i + 1]:
            www.append(mid)
            count += 1
            mid += k + 1

    # print(w + test + ww)
    print(w, ww, www)
    print(count)