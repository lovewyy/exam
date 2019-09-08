class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode3 = ListNode(3)
listNode4 = ListNode(5)
listNode5 = ListNode(6)
listNode1.next = listNode2
listNode2.next = listNode3
listNode3.next = listNode4
listNode4.next = listNode5

# print(listNode3.next.value)

def reverseListNode(head):
    if head is None:
        return head
    last = None
    while head:
        temp = head.next
        head.next = last
        last = head
        head = temp
    return last

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

r1 = reverseListNode(listNode1)
print(r1.next.next.value)
r2 = reverseList(r1)
print(r2.next.next.value)
