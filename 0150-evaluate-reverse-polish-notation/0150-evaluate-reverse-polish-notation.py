class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for item in tokens:
            if item not in '+-*/':
                s.append(int(item))
            else:
                op2 = s.pop()
                op1 = s.pop()
                if item == '+':
                    s.append(op1 + op2)
                elif item == '-':
                    s.append(op1 - op2)
                elif item == '*':
                    s.append(op1 * op2)
                elif item == '/':
                    # truncate toward zero
                    s.append(int(op1 / op2))
        return s[0]