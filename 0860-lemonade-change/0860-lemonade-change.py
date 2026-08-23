class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s = 0
        l = 0

        for i in bills:
            if i == 5:
                s += 1
            elif i == 10:
                s -= 1
                l += 1
                if s < 0:
                    return False
            
            if i == 20:
                if l > 0:
                    l -= 1
                    s -= 1
                    if s < 0:
                        return False
                elif s > 2:
                    s -= 3
                else:
                    return False
            print(s,l)
        return True