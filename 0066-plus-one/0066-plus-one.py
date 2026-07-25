class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=0
        while i < len(digits):
            if digits[-(i+1)] < 9:
                digits[-(i+1)] += 1
                return digits
            elif (i+1) < len(digits):
                digits[-(i+1)] = 0
                i = i+1 
            else:
                digits[-(i+1)] = 0
                digits.insert(0, 1)
                return digits