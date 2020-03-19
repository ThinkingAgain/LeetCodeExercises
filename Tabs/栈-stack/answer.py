
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        """
        1013. 将数组分成和相等的三个部分
        给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
        形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] ==
        A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
        """
        if len(A) < 3 : return False
        if sum(A) % 3 != 0 : return False
        s = sum(A) / 3
        i = 0
        j = len(A) - 1
        while i + 1 < j:
            if sum(A[:i+1]) != s:
                i += 1
                continue
            if sum(A[j:]) != s:
                j -= 1
                continue
            print(f"{A[:i + 1]}--{A[i + 1:j]}--{A[j:]}")
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    a = [18,12,-18,18,-19,-1,10,10]

    print(s.canThreePartsEqualSum(a))
