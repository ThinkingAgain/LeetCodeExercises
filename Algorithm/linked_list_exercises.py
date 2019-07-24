# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ite = self
        tostring = str(ite.val)
        while ite.next != None:
            tostring += "->"+str(ite.next.val)
            ite = ite.next
        return tostring

class Solution:
    #用列表构造一个链表
    def constructNodelist(self, li:list)->ListNode:
        if (len(li) == 0):
            return None
        head = ListNode(li[0])
        tail = head
        for x in li[1:]:
            tail.next = ListNode(x)
            tail = tail.next
        return head

    #返回链表字符串

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

    """
    反转链表
    =============================
    反转一个单链表。
    示例:    
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    进阶:
    你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
    """
    def reverseList_iterator(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        newhead = head
        head = head.next
        newhead.next = None
        while head.next != None:
            oldhead = head.next
            head.next = newhead
            newhead = head
            head = oldhead
        head.next = newhead
        return head





if __name__ == "__main__":
    solution = Solution()

    li = [1, 2, 3, 4, 5]
    head = solution.constructNodelist(li)
    head = solution.reverseList_iterator(head)
    print(head)


