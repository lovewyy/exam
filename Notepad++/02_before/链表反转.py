class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseList(head):
    if head is None:
        return head
    last = None
    while head:
        temp = head.next
        head.next = last
        last = head
        head = temp
    return last
    
t1 = listNode(1)
t2 = listNode(2)
t3 = listNode(3)
t4 = listNode(4)
t5 = listNode(5)
t6 = listNode(6)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5
t5.next = t6
print(t1==reverseList(reverseList(t1)))
r2 = reverseList(t1)
print(r2.next.next.value)