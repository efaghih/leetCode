class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        cnt_map = {}

        for i in range(len(nums)):
            cnt_map[nums[i]] = 0
            print (cnt_map)

        for i in range(len(nums)):
            for key in cnt_map.keys():
                if key > nums[i]:
                    cnt_map[key] += 1
        print(cnt_map)

        lst = []
        for num in nums:
            lst.append(cnt_map[num])
        return lst