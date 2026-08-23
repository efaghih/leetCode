class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # max_w = 0
        # for cstm in accounts:
        #     curr_w = sum(cstm)
        #     if (curr_w > max_w):
        #         max_w = curr_w
        
        # return max_w

        return max(map(sum, accounts))
