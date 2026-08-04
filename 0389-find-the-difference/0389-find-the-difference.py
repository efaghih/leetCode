class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ## Sol1:
        # for char in t:
        #     if char not in s:
        #         return char
        
        ## Sol2:
        # check_lst = {}
        # for char in s:
        #     check_lst[char] = check_lst.get(char, 0) + 1
        
        # for char in t:
        #     if check_lst.get(char, 0) == 0:
        #         return char
        #     elif check_lst.get(char) != 0:
        #         check_lst[char] = check_lst.get(char, 0) - 1
        

        ## Sol3:
        result = 0

        for c in s + t:
            result ^= ord(c)

        return chr(result)