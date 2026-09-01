class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        # Base points
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        # Initial differences
        dx0 = x1 - x0
        dy0 = y1 - y0
        
        # Check all remaining points starting from index 2
        for x, y in coordinates[2:]:
            curr_dx = x - x0
            curr_dy = y - y0
            
            # Cross-multiplication check
            if dy0 * curr_dx != dx0 * curr_dy:
                return False
                
        return True