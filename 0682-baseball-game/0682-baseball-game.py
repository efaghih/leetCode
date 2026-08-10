class Solution:
    def calPoints(self, operations: List[str]) -> int:
        oper = "+DC"
        rec = []
        for op in operations:
            if op not in oper:
                rec.append(int(op))
            
            if op == '+' and len(operations) > 1:
                
                a = rec.pop()
                b = rec.pop()
                rec.append(b)
                rec.append(a)
                rec.append(a+b)
            
            if op == 'D':
                a = rec.pop()
                rec.append(a)
                rec.append(a*2)
            
            if op == 'C':
                rec.pop()
            print(rec)
        return sum(rec)

            