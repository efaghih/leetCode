class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        #actual sum:
        n = len(nums)
        actSum = n * (n+1) // 2

        for i in nums:
            actSum -= i
        
        return actSum