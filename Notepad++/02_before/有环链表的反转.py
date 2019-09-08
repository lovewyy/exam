loc = locals()
def gvn(variable):
    for key in loc:
        if loc[key] == variable:
            return key

class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def reverseList(head):
    if head is None or head.next is None:
        return head
    last = None
    # a = set()
    # while head and head not in a:
    while head:
        # a.add(head)
        temp = head.next
        head.next = last
        last = head
        head = temp
    return last

def hasCycle(head):
    flag = "无环"
    if head is None:
        return flag
    fast = head.next.next
    slow = head.next
    while fast is not slow:
        if fast.next.next is None or fast.next is None:
            return flag
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            flag = "有环"
    if flag == "有环":
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        flag = "入环节点为%s,值为%d" %(gvn(fast), fast.value)
    return flag

def printList(head):
    a = set()
    while head is not None and head not in a:
        print("node: ", gvn(head), "value: ", head.value, "next: ", gvn(head.next))
        a.add(head)
        head = head.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n3

print(hasCycle(n1))
a1 = reverseList(n1)
printList(a1)