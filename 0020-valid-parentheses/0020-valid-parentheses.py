class Solution(object):
    def isValid(self, s):
        pairs = ["()", "{}", "[]"]
        while "()" in s or "{}" in s or '[]' in s:
            for p in pairs:
                s = s.replace(p, "")
        return s == ''