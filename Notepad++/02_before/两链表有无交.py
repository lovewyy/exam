class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def twoHas(head1, head2):
    flag = False
    s = set()
    if head1 is None or head2 is None:
        return flag
    while head1.next:
        s.add(head1.next)
        head1 = head1.next
    while head2:
        if head2 in s:
            flag = head2.value
            break
        head2 = head2.next
    return flag
    
    
    

t1 = listNode(1)
t2 = listNode(1)
t3 = listNode(3)
t4 = listNode(4)
t5 = listNode(5)
t6 = listNode(6)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5
t5.next = t6

a1 = listNode(11)
a2 = listNode(22)
a3 = listNode(33)
a4 = listNode(44)
a5 = listNode(55)
a1.next = a2
a2.next = a3
a3.next = t4


print(twoHas(t1,a1))
