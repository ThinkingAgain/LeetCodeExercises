"""
有效的字母异位词
=================================================================
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
--------------------------------------
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true
---------------------------------------
示例 2:
输入: s = "rat", t = "car"
输出: false
---------------------------------------
说明:
你可以假设字符串只包含小写字母。
进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
def isAnagram(s, t):
    if(set(s) != set(t)):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

"""
 验证回文字符串
 ===============================================================================
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
-----------------------------------------
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
--------------------------------------
示例 2:
输入: "race a car"
输出: false
--------------------------------------
"""
def isPalindrome(s: str) -> bool:
    isp = "".join([x for x in s if x.isalnum()]).lower()
    return isp == isp[::-1]

"""
字符串转换整数 (atoi)
==========================================================
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""
def myAtoi(str: str) -> int:
    MAX = 2**31 - 1
    MIN = -2**31
    str = str.lstrip()
    if len(str) == 0 :
        return 0
    if str[0].isdigit() or ( str[0] in ["+", "-"] and len(str) > 1 and str[1].isdigit()):
        end = 1
        for i in range(1, len(str)):
            if not str[i].isdigit():
                break;
            end += 1
        x = int(str[:end])
        if x > MAX:
            return MAX
        if x < MIN:
            return MIN
        return x
    return 0

"""
实现strStr()
===========================================
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""
def strStr(haystack: str, needle: str) -> int:
    return 0 if len(needle) == 0 else haystack.find(needle)

"""
报数
===========================
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。
"""
def countAndSay(n: int) -> str:
    seq = "1"
    for i in range(n):
        res = seq
        newseq = ""
        n = 0
        while n < len(seq):
            x = n+1
            while(x < len(seq) and seq[x] == seq[n]):
                x += 1
            newseq += str(x-n)+seq[n]
            n = x
        seq = newseq
    return res

"""
 最长公共前缀
 =====================================
 编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""
def longestCommonPrefix(strs) -> str:
    if len(strs) == 0 or strs[0] == "":
        return ""
    if len(strs) == 1:
        return strs[0]
    num = 0
    for i in range(len(strs[0])):
        comm = strs[0][i]
        for x in strs:
            if len(x) <= i or x[i] != comm:
                num = i
                break
        else:
            num = i + 1
            continue
        break
    return strs[0][:num]







if __name__ == "__main__":
    s = "abc"
    t = ["dog","racecar","car"]
    print(longestCommonPrefix(t))