class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i in range(len(s)):
            
            while j in range(len(t)):
                if s[i] == t[j]:
                    j += 1
                    break
                j += 1
            print("I: {} , J: {}".format(i, j))
            if (j == len(t)) and (i != len(s)-1):
                return False

            i += 1
        return True
        