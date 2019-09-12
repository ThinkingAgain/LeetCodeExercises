from typing import List

class Solution:
    """
    爬楼梯
    ===============================
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    """
    def climbStairs(self, n: int) -> int:
        #return n if n < 3 else self.climbStairs(n-1) + self.climbStairs(n-2)
        if n < 3: return n
        m1 = 2
        m2 = 1
        counts = 0
        for i in range(3, n+1):
            counts = m1 + m2
            m1, m2 = counts, m1
        return counts

    """
    买卖股票的最佳时机
    ============================================
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票），
    设计一个算法来计算你所能获取的最大利润。
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        profit = 0
        min = prices[0]
        for x in prices:
            profit = x - min if x - min > profit else profit
            min = x if x < min else min
        return profit

        """
        profit = 0
        while len(prices) > 1:
            imax = prices.index(max(prices))
            if imax == 0:
                prices.pop(0)
                continue
            left = prices[:imax + 1]
            profit = max(left) - min(left) if max(left) - min(left) > profit else profit
            prices = prices[imax + 1:]
        return profit
        """



    def maxSubArray(self, nums: List[int]) -> int:
        """
           最大子序和
           ====================================
           给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
           示例:
           输入: [-2,1,-3,4,-1,2,1,-5,4],
           输出: 6
           解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
           """
        maxs = max(nums)
        left = 0
        while len(nums) > 0 and nums[0] < 1: nums.pop(0)
        while len(nums) > 0 and nums[-1] < 1: nums.pop(-1)

        while len(nums) > 0:
            while len(nums) > 0 and nums[0] >= 0: left += nums.pop(0)
            if left > maxs:
                maxs = left
                nums.insert(0, left)
                nums.reverse()
                left = nums.pop(0)
            else:
                while len(nums) > 0 and nums[0] < 0: left += nums.pop(0)
                if left < 0: left = nums.pop(0)
        return maxs

    def rob(self, nums: List[int]) -> int:
        """
        打家劫舍
        ==========================
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是
        相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
        给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
        示例 1:
        输入: [1,2,3,1]
        输出: 4
        解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
        偷窃到的最高金额 = 1 + 3 = 4 。
        """
        N = len(nums)
        if N == 0 : return 0
        if N <= 2: return max(nums)
        dp = []
        dp.append(nums[0])
        dp.append( max(nums[0], nums[1]))
        for i in range(2, N):
            dp.append( max(dp[i-1], dp[i-2] + nums[i]))
        return max(dp)




if __name__ == "__main__":
    solution = Solution()

    #aa=set(range(2, 10))^set([x for x in range(10) for i in range(2, x) if x % i == 0])
    nums =  [2,7,9,3,1]
    print(solution.rob(nums))





