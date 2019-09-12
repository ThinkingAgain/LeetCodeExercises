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

        def isvalid(root: TreeNode):
            if root.left == None and root.right == None:
                return True, root.val, root.val
            if root.left == None:
                rtorf, rmin, rmax = isvalid(root.right)
                if rtorf and root.val < rmin:
                    return True, root.val, rmax
                else:
                    return False, None, None
            if root.right == None:
                ltorf, lmin, lmax = isvalid(root.left)
                if ltorf and root.val > lmax:
                    return True, lmin, root.val
                else:
                    return False, None, None
            ltorf, lmin, lmax = isvalid(root.left)
            rtorf, rmin, rmax = isvalid(root.right)
            if ltorf and rtorf and root.val > lmax and root.val < rmin:
                return True, lmin, rmax
            return False, None, None

        return isvalid(root)[0]

    '''
    对称二叉树
    ==========================
    给定一个二叉树，检查它是否是镜像对称的。
    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。    
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
     1
   / \
  2   2
   \   \
   3    3
    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(l:TreeNode, r:TreeNode)->bool:
            if l.val != r.val : return False
            if l.left == None and r.right == None and l.right == None and r.left == None: return True
            if l.left == None and r.right == None:
                if l.right == None or r.left == None:return False
                return isSym(l.right, r.left)
            if l.right == None and r.left == None:
                if l.left == None or r.right == None: return False
                return isSym(l.left, r.right)
            if l.left == None or r.right == None or l.right == None or r.left == None: return False
            return isSym(l.left, r.right) and isSym(l.right, r.left)
        if root == None: return True
        if root.left == None and root.right == None : return True
        if root.left == None or root.right == None: return  False
        return isSym(root.left, root.right)

    '''
    二叉树的层次遍历
    ==============================
    给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
    例如:
    给定二叉树: [3,9,20,null,null,15,7],    
        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：    
    [
      [3],
      [9,20],
      [15,7]
    ]
    '''
    def levelOrder(self, root: TreeNode) :
        dict = {}
        def lo (root:TreeNode, dict:dict, level:int):
            if root == None: return
            if level in dict:
                dict[level].append(root.val)
            else:
                dict[level] = [root.val]
            lo(root.left, dict, level+1)
            lo(root.right, dict, level+1)
        level = 0
        lo(root, dict,level)
        result = []
        for key, val in dict.items():
            result.append(val)
        return result

    '''
    将有序数组转换为二叉搜索树
    =================================
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    示例:
    给定有序数组: [-10,-3,0,5,9],
    一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
         0
        / \
      -3   9
      /   /
    -10  5
    '''
    def sortedArrayToBST(self, nums:list) -> TreeNode:
        if len(nums) == 0: return None
        if len(nums) == 1:return TreeNode(nums[0])

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = None if mid == len(nums)-1 else self.sortedArrayToBST(nums[mid +1:])

        return root









if __name__ == "__main__":
    bt = BinaryTree()
    a = [-10,-3,0,5,9]
    #tt=bt.constructor(a)
    tt = bt.sortedArrayToBST(a)
    print(bt.levelOrder(tt))
    print(tt)
    print(tt.left)
    print(tt.right)


