def returnnum(word: str) -> int:
        b = list(map(ord,list(word)))
        c = [str(i-97) for i in b]
        return int(''.join(c))

class Solution:       
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return returnnum(firstWord)+returnnum(secondWord)==returnnum(targetWord)        
