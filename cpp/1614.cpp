#include<algorithm>
class Solution {
public:
    int maxDepth(string s) {
        std::stack<char> st;
        int count1 = 0;
        for(int i=0;i<s.size();i++){
            if (s[i]=='('){
                st.push('(');
            }
            else if(s[i]==')'){
                st.pop();
            }
            count1 = count1>st.size()?count1:st.size();
        }
        return count1;
    }
};
