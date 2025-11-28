class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        print(len(s))
    
        if len(s) < 2:
            return False
        if len(s) % 2 != 0:
            return False

        for ch in s:
            if ch in ['(', '{', '[']:
                stk.append(ch)
            elif ch == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            elif ch == '}':
                if stk and stk[-1] == '{':
                    stk.pop()
                else:
                    return False
            elif ch == ']':
                if stk and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
            else:
                return False

        

        return stk == []
            
