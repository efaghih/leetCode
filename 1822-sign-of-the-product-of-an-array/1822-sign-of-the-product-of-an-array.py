class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else :
                return 0

        # cnt = 0
        # for n in nums:
        #     if n == 0:
        #         return 0
        #     if n < 0:
        #         cnt += -signFunc(n)
        # print (cnt)
        # return 1 if cnt % 2 == 0 else -1

        cnt = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                cnt *= signFunc(n)
        return cnt