class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = []
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        print(len(l))
        for i in words:
            str1 = ''
            for j in i:
                str1+=l[ord(j)-ord('a')]
            if str1 not in res:
                res.append(str1)
        return len(res)
            
