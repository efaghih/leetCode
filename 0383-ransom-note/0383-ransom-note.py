class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = magazine
        r = ransomNote
        map = {}

        for i in range(len(m)):
            map[m[i]] = 1 + map.get(m[i], 0)


        for i in range(len(r)):
            if map.get(r[i], 0) > 0:
                map[r[i]] -= 1
            else:
                return False
        return True