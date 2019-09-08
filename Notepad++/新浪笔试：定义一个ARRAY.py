class Array:
    def __init__(self, a, n1):
        self.a = a
        self.n1 = n1
    

    def num1(self, n):
        b = []
        result = 0
        r = 0
        value = n
        while value:
            r = value % 10
            b.append(r)
            value = int(value / 10)
        t = 1
        for i in range(0, len(b)-1):
            result += t * b[i]
            t *= 10
        return result
    
    def fun(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.num1(self.a[i]) > self.num1(self.a[j]):
                    temp = self.a[i]
                    self.a[i] = self.a[j]
                    self.a[j] = temp

    def printA(self):
        for i in self.a:
            print(i, end = '|')
        print()

a = [134, 445, 423, 233, 811]
test = Array(a, 5)
test.fun()
test.printA()
