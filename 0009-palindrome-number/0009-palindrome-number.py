class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        for i in range(len(num)//2):
            print(num[i], i)
            if num[i] != num[-(i + 1)]:
                return False
        return True