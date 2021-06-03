class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal=0
        if x>=0:
            if str(x)==str(x)[::-1]:
                pal=1           
        else:
            pal = 0
            
            
        if pal==0:
            return False
        else:
            return True
        
