
class MyHashSet(object):
    N = 49999
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [[] for _ in range(self.N)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % self.N
        if key not in self.hashset[i]:
            self.hashset[key % self.N].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % self.N
        if key in self.hashset[i]:
            self.hashset[i].pop(self.hashset[i].index(key))

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashset[key % self.N]


class MyHashMap(object):
    N = 6869
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = [[[],[]] for _ in range(self.N)]

    def myhash(self, key):
        return key % self.N

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        ha = self.myhash(key)
        if key not in self.hashmap[ha][0]:
            self.hashmap[ha][0].append(key)
            self.hashmap[ha][1].append(value)
        else:
            self.hashmap[ha][1][self.hashmap[ha][0].index(key)] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        ha = self.myhash(key)
        if key not in self.hashmap[ha][0]:
            return -1
        else:
            return self.hashmap[ha][1][self.hashmap[ha][0].index(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        ha = self.myhash(key)
        if key in self.hashmap[ha][0]:
            i = self.hashmap[ha][0].index(key)
            self.hashmap[ha][0].pop(i)
            self.hashmap[ha][1].pop(i)

if __name__ == "__main__":
    hashSet = MyHashSet()



    hashMap = MyHashMap()
    hashMap.put(1, 10)
    hashMap.put(2, 2)
    print(hashMap.get(1)) # 返回 1
    print(hashMap.get(3)) # 返回 - 1(未找到)
    hashMap.put(2, 1)# 更新已有的值
    print(hashMap.get(2)) # 返回   1
    hashMap.remove(2) # 删除键为2的数据
    print(hashMap.get(2)) # 返回 - 1(未找到)
    print(hashMap.myhash(65513))

