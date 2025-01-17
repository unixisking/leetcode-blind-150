class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSet = set(s)
        for char in sSet:
            if s.count(char) != t.count(char):
                return False
        return True
