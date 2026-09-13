import re, math
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s= s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()

        left, right = 0, len(s)
        half = math.ceil(right/2)
        
        while left < half:
            if s[left] != s[right-1]:
                return False
            left,right = left+1, right-1
        
        
        return True

        