class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 哈希解法
        if len(s) != len(t):
            return False
        temp = {}
        for c in s:
            temp[c] = temp.setdefault(c, 0) + 1
        for c in t:
            if c not in temp or temp[c] < 1:
                return False
            temp[c] -= 1
        return True

    def isAnagram_02(self, s: str, t: str) -> bool:
        # 哈希解法变形，使用自定义的数组代替哈希表
        if len(s) != len(t):
            return False
        temp = [0] * 27
        for c in s:
            temp[ord(c)-ord("a")] += 1
        for c in t:
            temp[ord(c)-ord("a")] -= 1
            if temp[ord(c)-ord("a")] < 0:
                return False
        return True

    def isAnagram_03(self, s: str, t: str) -> bool:
        # 使用内置的 count 函数
        if len(s) != len(t):
            return False
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True

    def isAnagram_04(self, s: str, t: str) -> bool:
        # 使用内置的 sorted 函数
        return sorted(s) == sorted(t)
