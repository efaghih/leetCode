class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        s = []
        res = []
        for num in range(1, n+1):
            s.append(num)
            res.append("Push")

            if s and s[-1] not in target:
                s.pop()
                res.append("Pop")
            if s == target:
                break
        return (res)