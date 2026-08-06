class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s = sorted(arr)
        if len(s) < 2:
            return False

        rng = s[1] - s[0]
        for i in range(1, len(s) - 1):
            if (s[i+1] - s[i]) != rng:
                return False
            
        return True
