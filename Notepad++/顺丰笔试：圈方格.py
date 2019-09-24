#
for i in range(34):
    space = i
    res = 0
    init = 3
    k = 0
    t = 0
    while res < space:
        k = init // 4 
        
        if init % 4 == 3:
            res += (2 * k + 1) * 0.5
            
        elif init % 4 == 0:
            res += (2 * k + 1) * 0.5
            
        elif init % 4 == 1:
            res += (2 * k - 1) * 0.5
            
        elif init % 4 == 2:
            res += (2 * k + 1) * 0.5
        
        if res >= space:
            t = init
            break
        
        init += 1

    print(i, t)