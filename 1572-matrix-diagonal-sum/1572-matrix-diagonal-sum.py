class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        cnt = 0
        rcnt = len(mat[0])-1
        print(rcnt)
        s = 0
        for i in mat:
            if (rcnt - cnt) != cnt:
                s += i[cnt] + i[rcnt - cnt]
                cnt += 1
            else:
                s += i[cnt]
                cnt += 1
        return s