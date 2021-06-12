class Solution:
    def reverseVowels(self, s: str) -> str:
        b = []
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                b.append(i)
                
        c = list(s)
        print(c,b)
        j = -1
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                c[i] = s[b[j]]
                j = j-1
        
        return ''.join(c)
                
        
                
            
            
