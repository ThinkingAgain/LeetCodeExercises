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

    """ 
    二叉树的最大深度
    =============================
    给定一个二叉树，找出其最大深度。
    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    """
    验证二叉搜索树
    ==========================
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。
    假设一个二叉搜索树具有如下特征：    
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left != None and root.left.val > root.val:
                return False
        if (root.right != None and root.right.val < root.val):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)






if __name__ == "__main__":
    bt = BinaryTree()
    a = [2,1,4,None,None,3,6]
    tt=bt.constructor(a)
    print(bt.isValidBST(tt))


