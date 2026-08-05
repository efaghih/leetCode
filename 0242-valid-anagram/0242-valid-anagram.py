class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cl = {}
        if len(s) != len(t):
            return False

        for char in s:
            cl[char] = cl.get(char, 0) + 1
        
        for char in t:
            cl[char] = cl.get(char, 0) - 1
            if cl[char] < 0:
                return False
        return True