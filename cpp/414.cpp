class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> num(nums.begin(),nums.end());
        vector<int> numb(num.begin(),num.end());
        sort(numb.begin(),numb.end());
        if (numb.size()>2){
            return numb[numb.size()-3];
        }
        else{
            return numb[numb.size()-1];
        }
    }
};
