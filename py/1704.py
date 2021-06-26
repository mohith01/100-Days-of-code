class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 =0
        count2 = 0
        b = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        str1 = s[:len(s)//2]
        str2 = s[(len(s)//2):]
        print(str1,str2)
        for i in b:
            if i in str1:
                count1+=str1.count(i)
            if i in str2:
                count2+=str2.count(i)
        
        return count1==count2
