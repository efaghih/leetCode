# import random

# class Solution:

#     def __init__(self, w: list[int]):
#         self.wth = w
#         # 1. Precompute the total sum once during initialization
#         self.sumW = sum(w)        

#     def pickIndex(self) -> int:
#         if not self.wth:
#             return 0

#         # 2. Use random.random() for full float precision (0.0 to 1.0)
#         x = random.random()
        
#         window = 0
#         for idx, num in enumerate(self.wth):
#             window += num / self.sumW
            
   
#             if x < window:
#                 return idx
                
    
#         return len(self.wth) - 1



import random
import bisect
class Solution:

    def __init__(self, w: list[int]):
        self.wth = w
        self.sumW = []
        curr = 0
        for num in self.wth:
            curr += num
            self.sumW.append(curr)
        self.total = curr


    def pickIndex(self) -> int:
        if not self.wth:
            return 0
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.sumW, target)