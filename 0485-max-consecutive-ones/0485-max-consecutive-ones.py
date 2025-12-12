class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if len(nums) == 1 and nums[0] == 1:
            return 1
        elif nums[:] == [0]*len(nums):
            return 0
        i = 0
        cnt = 1
        mx = 0
        
        while i < len(nums)-1:
            if nums[i] == 1:
                if nums[i] ^ nums[i+1] == 0:
                    cnt += 1
                    print("here")
                    print("cnth: ", cnt)
            else:
                print("i:", i)
                print("cnt: ", cnt)
                cnt = 1
            i += 1
            mx = max(mx, cnt)
        return mx