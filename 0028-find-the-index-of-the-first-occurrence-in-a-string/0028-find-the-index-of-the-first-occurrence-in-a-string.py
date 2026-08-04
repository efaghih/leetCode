class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
                # for i in range(len(haystack) - len(needle) + 1):
                #     if haystack[i:i+len(needle)] == needle:
                #         return i
                # return -1

                for i in range (len(haystack) - len(needle) + 1):
                    ch = haystack[i]
                    cn = needle[0]
                    if ch == cn:
                        if haystack[i:i+len(needle)] == needle:
                            return i
                        else: continue
                return -1