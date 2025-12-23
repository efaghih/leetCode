class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        exst_mp = {}
        prev = 0
        dob = 0
        for i in range(len(nums)):
            exst_mp[nums[i]] = 1 + exst_mp.get(nums[i], 0)
        print(dob)
        print(exst_mp)
        missed = 0
        for i in range(1, len(nums) + 1):
            if i not in exst_mp.keys() and missed == 0:
                missed = i
            if (i < len(nums)) and exst_mp[nums[i]] == 2:
                dob = nums[i]

        return [dob, missed]
