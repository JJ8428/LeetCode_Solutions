# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        nodes = []
        node = head
        nodes = [head]
        while not node.next is None:
            node = node.next
            nodes.append(node)
        if n != nodes.__len__() and n != 1:
            print("a")
            nodes[(n*-1)-1].next = nodes[(n*-1)+1]
        elif n == 1:
            print("b")
            if nodes.__len__() == 1:
                head = None
            else:
                nodes[-2].next = None
        elif n == nodes.__len__():
            print("c")
            if nodes.__len__() == 1:
                head = None
            else:
                head = head.next
        return head
        