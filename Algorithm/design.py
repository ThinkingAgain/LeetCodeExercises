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
        self.mini_stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.mini_stack.append(x)
        self.min = x if self.min is None else min(x, self.min)

    def pop(self) -> None:
        if self.min == self.mini_stack.pop():
            self.min = min(self.mini_stack) if self.mini_stack else None


    def top(self) -> int:
        return self.mini_stack[-1]

    def getMin(self) -> int:
        return self.min




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    mi = MinStack()
    mi.push(3)
    mi.push(8)
    print(mi.mini_stack)
    print(mi.min)

    mi.push(1)
    mi.push(5)
    mi.push(9)
    mi.push(4)
    print(mi.mini_stack)

    print(mi.min)
    mi.pop()
    print(mi.mini_stack)


    print(mi.top())
    mi.pop()
    mi.pop()
    mi.pop()
    print(mi.mini_stack)
    print(mi.getMin())