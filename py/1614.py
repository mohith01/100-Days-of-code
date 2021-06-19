class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = []
        for i in s:
            if i=='(':
                res.append('(')
            elif i==')':
                res.pop()
            count = max(len(res),count)
            
        return count
        
