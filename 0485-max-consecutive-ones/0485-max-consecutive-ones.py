class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        mx = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i
                while (j in range(len(nums))) and (nums[j] == 1):
                    j += 1
                    cnt += 1
                mx = max(mx, cnt)
                i += cnt
                cnt = 0
                continue
            i += 1
        return mx


        