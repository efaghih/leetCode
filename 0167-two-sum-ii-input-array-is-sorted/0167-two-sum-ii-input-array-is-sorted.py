class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0 
        r = 1
        sum = 0
        while l < len (numbers)-1:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                sum -= numbers[r]
                r += 1
            else: 
                sum = 0
                l += 1
                r = l+1
                