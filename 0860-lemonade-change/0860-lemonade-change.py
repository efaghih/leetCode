class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s = 0  # $5 bills
        l = 0  # $10 bills

        for bill in bills:
            if bill == 5:
                s += 1

            elif bill == 10:
                if s == 0:
                    return False
                s -= 1
                l += 1

            elif bill == 20:
                # Prefer using $10 + $5
                if l > 0 and s > 0:
                    l -= 1
                    s -= 1

                # Otherwise use three $5 bills
                elif s >= 3:
                    s -= 3

                else:
                    return False

        return True
