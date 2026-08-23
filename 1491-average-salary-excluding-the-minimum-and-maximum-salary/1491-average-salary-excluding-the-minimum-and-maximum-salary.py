class Solution:
    def average(self, salary: List[int]) -> float:
        
        s = 0
        s -= max(salary)
        s -= min(salary)
        
        s += sum(salary)
        
        return s / (len(salary) - 2) 