class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}

        for i, val in enumerate(nums):
            map[val] = 1 + map.get(val, 0) 
        print(map)

        mx = max(map.values())
        for k, v in map.items():
            if v == mx:
                return k

