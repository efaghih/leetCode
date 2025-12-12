class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i] , 0)
        print(map)
        for key , val in map.items():
            if val == 1:
                return key