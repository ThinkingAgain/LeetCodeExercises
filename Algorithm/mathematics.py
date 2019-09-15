from typing import List
import math


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Fizz Buzz
        ==================
        写一个程序，输出从 1 到 n 数字的字符串表示。
        1. 如果 n 是3的倍数，输出“Fizz”；
        2. 如果 n 是5的倍数，输出“Buzz”；
        3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
        :param n:
        :return:
        """
        return ["FizzBuzz" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else
                "Buzz" if x % 5 == 0 else str(x) for x in range(1, n+1)]

    def countPrimes(self, n: int) -> int:
        """
         计数质数
         =========================
         统计所有小于非负整数 n 的质数的数量。
        :param n:
        :return:
        """
        if n < 3:return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
        return sum(primes)

    def isPowerOfThree(self, n: int) -> bool:
        """
        3的幂
        =====================
        给定一个整数，写一个函数来判断它是否是 3 的幂次方。
        :param n:
        :return:
        """
        for i in range(n):
            x = 3**i
            if x == n:return True
            if x > n:return False
        return False

    def romanToInt(self, s: str) -> int:
        """
        罗马数字转整数
        ===========================
        罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
        通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
        所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
        给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
        :param s:
        :return:
        """
        if len(s) == 0: return 0
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        trans = []
        for x in s:
            trans.append(roman[x])
        res = trans[-1]
        for i in range(len(trans)-1):
            res += trans[i] if trans[i] >= trans[i+1] else -trans[i]
        return res






if __name__ == "__main__":
    so = Solution()

    s = "MCMXCIV"
    print(so.romanToInt(s))

