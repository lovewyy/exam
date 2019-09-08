class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def hasCycle(head):
    flag = False
    if head is None:
        return flag
    fast = head.next.next
    slow = head.next
    while fast is not slow:
        if fast.next is None or fast.next.next is None:
            return flag
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            flag = True
    # find the entrance
    if flag == True:
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast.value

if __name__ == "__main__":
    n1 = listNode(1)
    n2 = listNode(2)
    n3 = listNode(3)
    n4 = listNode(4)
    n5 = listNode(5)
    n6 = listNode(6)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n3

    print(hasCycle(n1))