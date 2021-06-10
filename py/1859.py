class Solution:
    def sortSentence(self, s: str) -> str:
        res = s.split(' ')
        b = list(range(len(res)))
        for i in res:
            print(i)
            b[int(i[-1])-1] = i[:-1]
            
        return ' '.join(b)
            
