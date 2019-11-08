class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.random_set:
            return False
        else:
            self.random_set.add(val)
            return True;

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.random_set:
            return False
        else:
            self.random_set.remove(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_element = self.random_set.pop()
        self.random_set.add(random_element)
        return random_element

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()