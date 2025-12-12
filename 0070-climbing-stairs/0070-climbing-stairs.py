class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        posWays = []
        for i in range(n+1):
            posWays.append(0)
        
        posWays[1] = 1
        posWays[2] = 2

        for i in range(3, n+1):
            posWays[i] = posWays[i-1] + posWays[i-2]
        return posWays[n]