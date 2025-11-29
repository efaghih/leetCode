class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = []
        tmp.append(nums[0])
        i = 0
        while i in range(len(nums)-1):
            nxt = nums[i+1]
            if (tmp[-1] == nxt):
                i += 1
                continue
            tmp.append(nums[i+1])
            i += 1
            
        nums[:] = tmp
