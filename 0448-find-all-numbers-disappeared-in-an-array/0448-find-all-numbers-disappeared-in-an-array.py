class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mis = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1 #abs in case of num became neg earlier
            if (nums[idx] > 0):
                nums[idx] = -nums[idx]
        print(nums)
       

        return [(i+1) for i in range(len(nums)) if nums[i] > 0]