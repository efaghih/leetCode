class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #boundary conditions 
        if len(s) <2:
            return len(s)
        if " " not in s:
            return len(s)

        #the rest conditions
        i = len(s) - 1 
        char = s[i]
        
        while char == " ":
            i -= 1
            char = s[i]
  
        j = i
        print(j)
        while char != " ":
            j -= 1
            char = s[j]
        
        return i-j