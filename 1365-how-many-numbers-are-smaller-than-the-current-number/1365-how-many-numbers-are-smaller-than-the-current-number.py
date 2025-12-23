class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sr = sorted(nums)
        cnt_mp = {} 
        for i in range(len(nums)):
            if sr[i] not in cnt_mp.keys():
                cnt_mp[sr[i]] = i
            
        return [cnt_mp[num] for num in nums]