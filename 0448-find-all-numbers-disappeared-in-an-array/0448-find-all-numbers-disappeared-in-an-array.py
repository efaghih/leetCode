class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        misList = []
        mis = {}
        for i in range(len(nums)):
            mis[nums[i]] = 1
   
        misList = []
        for i in range(len(nums)):
            if (i+1) not in mis:
                misList.append(i+1)
   