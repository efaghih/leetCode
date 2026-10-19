class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # Initialize dp with the first row's values
        dp = points[0][:]
        
        for r in range(1, m):
            new_dp = [0] * n
            
            # 1. Left-to-right pass
            left_max = 0
            for c in range(n):
                left_max = max(left_max - 1, dp[c])
                new_dp[c] = left_max
                
            # 2. Right-to-left pass and combine with the current row's points
            right_max = 0
            for c in range(n - 1, -1, -1):
                right_max = max(right_max - 1, dp[c])
                new_dp[c] = max(new_dp[c], right_max) + points[r][c]
                
            dp = new_dp
            
        return max(dp)