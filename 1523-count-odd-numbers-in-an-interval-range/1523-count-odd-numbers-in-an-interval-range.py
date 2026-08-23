class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # odds = 0
        # for i in range(low, high+1, 1):
        #     if i%2 != 0:
        #        odds += 1
          
        # return odds

        odds = high - low
        if high % 2 == 0 and low % 2 == 0:
            return (odds // 2)
        else:
            return (odds // 2) + 1
        
        
