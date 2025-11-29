class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        clnS = "".join(c.lower() for c in s if c.isalnum())
        
        l = 0
        r = len(clnS)-1


        while l < r:
            if clnS[l] != clnS[r]:
                return False
            l += 1
            r -= 1
        
        return True