import random

class Solution:

    def __init__(self, w: list[int]):
        self.wth = w
        # 1. Precompute the total sum once during initialization
        self.sumW = sum(w)        

    def pickIndex(self) -> int:
        if not self.wth:
            return 0

        # 2. Use random.random() for full float precision (0.0 to 1.0)
        x = random.random()
        
        window = 0
        for idx, num in enumerate(self.wth):
            window += num / self.sumW
            
            # 3. Clean check: as soon as our random number falls below the window, return the index
            if x < window:
                return idx
                
        # Fallback for extreme floating-point edge cases
        return len(self.wth) - 1