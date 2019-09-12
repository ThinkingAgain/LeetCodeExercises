from typing import List
import random

class Solution:
    """
    Shuffle an Array
    ---------------------------------
    打乱一个没有重复元素的数组。
    示例:
    // 以数字集合 1, 2 和 3 初始化数组。
    int[] nums = {1,2,3};
    Solution solution = new Solution(nums);
    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
    solution.shuffle();
    // 重设数组到它的初始状态[1,2,3]。
    solution.reset();
    // 随机返回数组[1,2,3]打乱后的结果。
    solution.shuffle();
    """

    def __init__(self, nums: List[int]):
        self.__origin = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.__origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuf = self.__origin[:]
        random.shuffle(shuf)
        return shuf

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


class MinStack:
    """
    最小栈
    =================================
    设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。
    示例:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__mini_stack = []
        self.__N = 0
        self.__min_index = None

    def push(self, x: int) -> None:
        self.__mini_stack.append(x)
        self.__N += 1

    def pop(self) -> None:
        self.__mini_stack.pop()
        self.__N -= 1

    def top(self) -> int:

    def getMin(self) -> int:


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    sol = Solution(nums)
    for _ in range(10):
        print(sol.shuffle())
    print(sol.reset())