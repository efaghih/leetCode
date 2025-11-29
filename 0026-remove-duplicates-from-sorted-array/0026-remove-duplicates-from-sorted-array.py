class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = len(nums)
        while i < k-1:
            nxt = nums[i+1]
            prev = nums[i]

            if (prev == nxt):
                del nums[i]
                k -= 1
                #i += 1
                continue
            i += 1
        
        
