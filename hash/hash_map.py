from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
        def __init__(self, x):
             self.val = x
             self.left = None
             self.right = None

        def __str__(self):
            s = str(self.val)
            s += " -- L: "
            s += "None" if self.left == None else str(self.left.val)
            s += "  R: "
            s += "None" if self.right == None else str(self.right.val)
            return s

class BinaryTree:
    """根据列表构造一个二叉树"""
    def constructor(self, alist:list) -> TreeNode:
        if len(alist) == 0:
            return None
        bt = [None]
        for x in alist:
            bt.append(TreeNode(x) if x != None else None)
        N = len(alist)
        for i in range(1,N+1):
            if bt[i] ==None:
                continue
            bt[i].left = None if 2*i > N else bt[2*i]
            bt[i].right = None if 2*i+1 > N else bt[2*i+1]
        return bt[1]

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
         同构字符串
         =====================
         给定两个字符串 s 和 t，判断它们是否是同构的。
         如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
         所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，
         但字符可以映射自己本身。
         示例 1:
         输入: s = "egg", t = "add"
         输出: true
        """
        if not s: return True
        test_s = {}
        test_t = {}
        for i in range(len(s)):
            if s[i] in test_s: test_s[s[i]].append(i)
            else: test_s[s[i]] = [i]
            if t[i] in test_t: test_t[t[i]].append(i)
            else: test_t[t[i]] = [i]
        for i in range(len(s)):
            if test_s[s[i]] != test_t[t[i]]: return False
        return True

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        两个列表的最小索引总和
        =========================
        假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

        """
        common = set(list1) & set(list2)
        res = {}
        minindex = len(list1) + len(list2)
        for x in common:
            index = list1.index(x)+ list2.index(x)
            minindex = min(minindex, index)
            if index in res : res[index].append(x)
            else: res[index] = [x]
        return res[minindex]

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        存在重复元素 II
        ======================
        给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，
        并且 i 和 j 的差的绝对值最大为 k。
        """
        dup = {}
        for i, x in enumerate(nums):
            if (i - dup[x] if x in dup else k + 1) <= k: return True
            dup[x] = i
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        字母异位词分组
        ==============================
        给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
        """
        store = {}
        for x in strs:
            k = "".join(sorted(list(x)))
            if k not in store: store[k] = [x]
            else: store[k].append(x)
        return list(store.values())


    def treeMapTuple(self, root:TreeNode) -> tuple:
        if not root : return (None,)
        return (root.val, self.treeMapTuple(root.left), self.treeMapTuple(root.right) )


    def iterTree(self, root:TreeNode, dup:collections.defaultdict):
        if not root:return
        dup[self.treeMapTuple(root)].append(root)
        self.iterTree(root.left, dup)
        self.iterTree(root.right, dup)

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        寻找重复的子树
        =======================
        给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
        两棵树重复是指它们具有相同的结构以及相同的结点值。
        """
        dup = collections.defaultdict(list)
        res = []
        self.iterTree(root, dup)
        for k, trees in dup.items():
            if len(trees) > 1: res.append(trees[0])

        return res


if __name__ == "__main__":
    so = Solution()

    bt = BinaryTree()
    a = [1, 2, 3, 4, None, 2, 4, None, None,None, None, 4]
    tt=bt.constructor(a)
    for x in so.findDuplicateSubtrees(tt):
        print(x.val)





