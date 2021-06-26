class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> res = {0};
        int max2 = 0;
        int max1 = 0;
        for (int i=1;i<gain.size()+1;i++){
            max2 = accumulate(gain.begin(),gain.begin()+i,0);
            if (max2>max1){
             max1 = max2;   
            } 
            }
        return max1;
    }
};
