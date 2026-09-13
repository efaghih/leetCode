class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
    
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
    
        # Multiply each digit starting from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Convert characters to single-digit integers using ord()
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                total = mul + pos[i + j + 1]
    
                pos[i + j + 1] = total % 10
                pos[i + j] += total // 10
    
        # Skip leading zeros
        start = 0
        while start < len(pos) and pos[start] == 0:
            start += 1
    
        # Convert the resulting list of digits back to a string
        return "".join(map(str, pos[start:]))
           
    

        