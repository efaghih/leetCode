class Solution:
    def romanToInt(self, s: str) -> int:
        map = {}
        map['I'] = 1
        map['V'] = 5
        map['X'] = 10
        map['L'] = 50
        map['C'] = 100
        map['D'] = 500
        map['M'] = 1000
        integer = 0
        for char in range(len(s)):
            integer += map[s[char]]
            if char < (len(s)-1): 
                nxChar = s[char+1]
                if s[char] == 'I' and ((nxChar == 'X') or (nxChar == 'V')):
                    integer -= 2* map['I']
                elif s[char] == 'X' and ((nxChar == 'L') or (nxChar == 'C')):
                    integer -= 2* map['X']
                elif s[char] == 'C' and ((nxChar == 'D') or (nxChar == 'M')):
                    integer -= 2* map['C']
            
        return integer   
          