class Solution {
public:
    int balancedStringSplit(string s) {
        int count = 0;
        int res = 0;
        for (int i =0 ;i<s.size();i++){
            count+=s[i]=='R'? 1:-1;
            if (count==0){
                res+=1;
            }
        }
        return res;
    }
};
