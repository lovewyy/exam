import sys

if __name__ == "__main__":
    # 读取第一行的n
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    n = [ [0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    result = 0
    m = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                n[i + 1][j + 1]=n[i][j] + 1
                if n[i + 1][j + 1] > result:
                    result = n[i + 1][j + 1]
                    m= i + 1
    print(result)

def findA(a, b):   
    n = [ [0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    result = 0
    m = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                n[i + 1][j + 1]=n[i][j] + 1
                if n[i + 1][j + 1] > result:
                    result = n[i + 1][j + 1]
                    m= i + 1
    return result

print(findA('abcbdab','bcdbda'))
