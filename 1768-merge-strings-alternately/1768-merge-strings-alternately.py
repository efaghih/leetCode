class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        min_len = min(len(word1), len(word2))
        
        for i in range (min_len):
            res += word1[i]
            res += word2[i]
        
        if len(word1) > len(word2):
            res += word1[len(word2):]
        else:
            res += word2[len(word1):]

        return res

        