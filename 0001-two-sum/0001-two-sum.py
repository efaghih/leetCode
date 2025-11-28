class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        
        nums = [-3,4,3,90]
        target = 0
        while i in range (len(nums)):
            if nums[i] <= target:
                j = i+1
                while j <  (len(nums)):
                    print("j-out: ", j)
                    print("nums[j]: ", nums[j])
                    if (nums[i] + nums[j]) == target:
                        return [i,j]
                    j += 1
            i += 1