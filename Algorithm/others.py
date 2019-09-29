class Solution(object):
    def hammingWeight(self, n):
        """
        位1的个数
        ===================================
        编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hammingDistance(self, x, y):
        """
        汉明距离
        =========================
        两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
        给出两个整数 x 和 y，计算它们之间的汉明距离。
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

    def reverseBits(self, n):
        """
         颠倒二进制位
         =========================
         颠倒给定的 32 位无符号整数的二进制位。
        :param n:
        :return:
        """

        return int(bin(n)[-32:].zfill(32)[::-1], 2)

    def generate(self, numRows):
        """
         帕斯卡三角形
         =====================
         给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1: return []
        res = []
        nrow = [1]
        for _ in range(numRows):
            res.append(nrow)
            t = [1]
            for i in range(1, len(nrow)):
                t.append(nrow[i-1] + nrow[i])
            t.append(1)
            nrow = t
        return res

    def isValid(self, s):
        """
         有效的括号
         =================================
         给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
         有效字符串需满足：
         左括号必须用相同类型的右括号闭合。
         左括号必须以正确的顺序闭合。
         注意空字符串可被认为是有效字符串。
        :type s: str
        :rtype: bool
        """
        if s == "": return True
        if len(s) % 2 == 1 : return False
        d = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stock = []
        for x in s:
            if x in d:
                stock.append(x)
            else:
                if not stock or d[stock.pop()] != x:
                    break
        else:
            if not stock: return True
        return False

    def missingNumber(self, nums):
        """
         缺失数字
         =====================
         给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
        :type nums: List[int]
        :rtype: int
        """
        res = [0] * (len(nums)+1)

        for x in nums:
            res[x] = 1
        return res.index(0)


if __name__ == "__main__":
    so = Solution()

    print(so.missingNumber([9,6,4,2,3,5,7,0,1]))