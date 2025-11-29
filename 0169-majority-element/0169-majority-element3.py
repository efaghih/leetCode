class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        n = len(nums)
        for i, val in enumerate(nums):
            map[val] = 1 + map.get(val, 0)
            if map[val] > (n/2):
                return val

        
        

