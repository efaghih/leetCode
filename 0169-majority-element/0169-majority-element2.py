class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}

        for i, val in enumerate(nums):
            map[val] = 1 + map.get(val, 0) 
        print(map)

        return max(map, key=map.get)
        

