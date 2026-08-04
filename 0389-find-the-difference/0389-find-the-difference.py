class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # for char in t:
        #     if char not in s:
        #         return char
        check_lst = {}
        for char in s:
            check_lst[char] = check_lst.get(char, 0) + 1
        
        for char in t:
            if check_lst.get(char, 0) == 0:
                return char
            elif check_lst.get(char) != 0:
                check_lst[char] = check_lst.get(char, 0) - 1
        