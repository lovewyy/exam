# 网易字符串解码或者展开

s = 'abc10[jr]a3[k]l'

def decodeS(s):
    stack = []
    now = ''
    num = 0
    for i in s:
        if i.isdigit():                         # 是数字，把数字和前一个数字相加
            num = num * 10 + int(i)
        elif i.isalpha():                       # 是字母，直接存进来
            now += i
        elif i == '[':                          # 是'['，存之前的字符串和数字；存完置为空和0
            stack.append((now, num))
            now = ''
            num = 0
        elif i == ']':                          # 结束了，把栈里面的取出来，和现在的now的字符串*数字（重新定义一个，避免改变num）
            before, nnum = stack.pop(-1)        # 注意不是num = 0，是nnum
            now = before + nnum * now
        else:
            return False
    return now

print(decodeS(s))


