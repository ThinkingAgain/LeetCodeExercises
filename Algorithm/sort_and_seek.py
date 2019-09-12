import sys


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 1: return True
    return False

class Solution:
    """
    合并两个有序数组
    ===========================================
    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    说明:
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    示例:
    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    输出: [1,2,2,3,5,6]
    """
    def merge(self, nums1, m: int, nums2 , n: int) -> None:
        for i in range(len(nums1) - m):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()

    """
    第一个错误的版本
    =======================================
    你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
    假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
    你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
    示例:
    给定 n = 5，并且 version = 4 是第一个错误的版本。
    ------------------------------------------------------
    调用 isBadVersion(3) -> false
    调用 isBadVersion(5) -> true
    调用 isBadVersion(4) -> true    
    所以，4 是第一个错误的版本。
    ----------------------------------------------------------- 
    """


    def firstBadVersion(self, n):
        version = [0]
        def testVersion(low, high, version):
            if low >= high: return low
            mid = (low + high) // 2
            if isBadVersion(mid):
                version[0] = mid
                return testVersion(low, mid -1, version)
            else:
                return testVersion(mid + 1, high, version)

        hit = testVersion(0, n, version)
        return hit if isBadVersion(hit) else version[0]







if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3

    for i in range(m):
        nums1.pop()
    nums1.extend(nums2)
    nums1.sort()
    print([(x,y,z) for x in range(5) for y in range(5) for z in range(5)
           if (x!=y)and(x!=z)and(y!=z)])
    print (solution.firstBadVersion(1))

