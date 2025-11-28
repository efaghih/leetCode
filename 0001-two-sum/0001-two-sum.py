class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in map and map[compl] != i:
                return [i, map[compl]]
