class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        mid = len(nums)//2
        start = 0
        end = len(nums)
        if not nums:
            return 0
        if target < nums[0]: 
            return 0
        if target > nums[-1]:
            return len(nums)

        while start < end:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
                mid = (end + start) // 2
            elif target > nums[mid]:
                start = mid + 1
                mid = (end + start) // 2

        
        return mid