class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        copArr = set()
        
        for i in nums:
            copArr.add(i)
        
            
        nums[:] = sorted(list(copArr))