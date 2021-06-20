class Solution {
public:
    int maxProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int res = nums.size()-1;
        return ((nums[res]-1)*(nums[res-1]-1));
    }
};
