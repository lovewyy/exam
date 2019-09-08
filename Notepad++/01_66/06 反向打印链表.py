# 06
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode3 = ListNode(3)
listNode1.next = listNode2
listNode2.next = listNode3

# 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead(listNode):
    # write code here
    if listNode == None:
          return []
    result = []
    while listNode:
        result.insert(0, listNode.val)
        listNode = listNode.next
    return result

print(printListFromTailToHead(listNode1))

def printListFromTailToHead2(listNode):
    if listNode != None:
        if listNode.next != None:
            printListFromTailToHead2(listNode.next)
        print(listNode.val, end = '**')

printListFromTailToHead2(listNode1)
print()

# 1、想到的：反转链表再打印，但是改变了链表

# 2、使用栈，先进先出
# list pop(index = -1)
# list 
test = [0, 1, 2, 3, 4, 3]
del test[2]
print(test)
test = [0, 1, 2, 3, 4, 3]
print('index:', test.index(3))
print(test.extend([1, 3, 4]), test)
test = []
print(test.insert(0, 10),test)
print('remove 10: ', test.remove(10), test)
print(test.count(3))

"""
删除对象：remove函数
删除索引：del 关键字
尾部删除一个：pop(index)
尾部插入一个：append(obj)
尾部插入多个：extend(list)
任意插入一个：insert(index, obj)
返回index：index(obj)
"""

test = [(1, 3), (2, 2), (1, 4), (3, 3)]
test.sort(key = lambda x:x[1], reverse = True)
print(test)

# 3、本质是递归，但是链表太长导致调用层级太深

