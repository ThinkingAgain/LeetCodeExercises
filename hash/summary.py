from typing import List
import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([x for x in S if x in J])

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        无重复字符的最长子串
        ==================================
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        !!需用滑动窗口来解决效率问题
        """
        start, maxlen = 0, 0
        d = {}
        for end, x in enumerate(s):
           if x in s[start:end]:
               maxlen = max(maxlen, end - start)
               start = d[x] + 1
           d[x] = end
        return max(maxlen, len(s[start:]))

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        四数相加 II
        ===========================
        给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
        使得 A[i] + B[j] + C[k] + D[l] = 0。
        为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
        所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
        """
        d = collections.defaultdict(int)
        res = 0
        for i,a in enumerate(A):
            for j,b in enumerate(B):
                d[a+b] += 1
        for c in C:
            for x in D:
                if -(c + x) in d.keys():
                    res += d[-(c + x)]
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
         前 K 个高频元素
         =================================
         给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
        """
        d = collections.defaultdict(int)
        for x in nums:
            d[x] += 1
        return [key for key, value in sorted(d.items(), key = lambda x:x[1], reverse=True)][:k]




















if __name__ == "__main__":
    so = Solution()

    print(so.topKFrequent([1,1,1,2,2,3], 2))

    d = {5:55, 1:11, 2:22, 3:33}
    a = sorted(d.items(), key = lambda x:x[1])



