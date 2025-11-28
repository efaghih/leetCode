class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mx = 0
        r = 0
        map = {}
        if len(s) <= 1:
            return len(s)
        while r < len(s):
            map[s[r]] = 1 + map.get(s[r], 0)
            if map[s[r]] > 1:
                map[s[r]] -= 1
                mx = max(r-l+1, mx)
                l += 1
                r += 1
                continue
            
            mx = max(r-l+1, mx)
            r += 1
        
        return mx