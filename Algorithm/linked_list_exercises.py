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

    """
    合并两个有序链表
    ========================
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
    示例：    
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodelist = []
        while l1 != None:
            nodelist.append(l1)
            l1 = l1.next
        while l2 != None:
            nodelist.append(l2)
            l2 = l2.next
        nodelist.sort(key=lambda y:y.val)
        for i in range(len(nodelist)-1):
            nodelist[i].next = nodelist[i+1]
        return nodelist[0] if nodelist else None

    """
    回文链表
    ======================
    请判断一个链表是否为回文链表。
    示例 1:    
    输入: 1->2
    输出: false
    示例 2:    
    输入: 1->2->2->1
    输出: true
    进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
    """
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        return a == a[::-1]

    """
    环形链表
    =================================
    给定一个链表，判断链表中是否有环。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = []
        while head != None:
            if head in a:
                return True
            a.append(head)
            head = head.next
        return False









if __name__ == "__main__":
    solution = Solution()

    li = [1,2,3,2,1]
    rl = solution.constructNodelist(li)
    print(solution.isPalindrome(rl))


