class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> res;
        int max = *max_element(candies.begin(),candies.end());
        for (int i : candies){
             res.emplace_back((i+extraCandies)>=max);
        }
    return res;
    }
};
