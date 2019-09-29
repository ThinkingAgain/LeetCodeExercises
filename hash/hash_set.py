class Solution(object):
    def intersection(self, nums1, nums2):
        """
        两个数组的交集
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))

    def isHappy(self, n):
        """
         快乐数
         =============================
         编写一个算法来判断一个数是不是“快乐数”。
         一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
         然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，
         那么这个数就是快乐数。
        :type n: int
        :rtype: bool
        """
        happy = {1}
        while n not in happy:
            happy.add(n)
            n = sum([int(x)**2 for x in str(n)])
        return True if n == 1 else False






if __name__ == "__main__":
    so = Solution()

    print(so.isHappy(7))