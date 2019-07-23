# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    删除链表中的节点
    ==================================
    请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
现有一个链表 -- head = [4,5,1,9]，它可以表示为:
    傻B题，实际就是删除首节点   """
    def deleteNode(self, node:ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if self.val == node.val:
            self = self.next
            return
        prev = self
        while prev.next != None:
            if prev.next.val == node.val:
                prev.next = prev.next.next
                return
            prev = prev.next
        return

    """
    删除链表的倒数第N个节点
    =============================
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = head
        end = head
        for i in range(n):
            end = end.next
        if end == None:
            prev = prev.next
            return prev
        while end.next != None:
            prev = prev.next
            end = end.next
        prev.next = prev.next.next
        return head


if __name__ == "__main__":
    head = None
    for i in range(5,0,-1):
        x = ListNode(i)
        x.next = head
        head = x
    """
        """
    solution = Solution()
    solution.removeNthFromEnd(head,2)
    while head != None:
        print(head.val)
        head = head.next


