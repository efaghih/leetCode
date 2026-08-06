class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s = sorted(arr)
        if len(s) < 2:
            return False

        rng = s[1] - s[0]
        for i in range(1, len(s)):
            if s[i] - s[i-1] != rng:
                return False
            
        return True

    
  