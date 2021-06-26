class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int mid,guess;
        int high = nums.size() - 1;
        while (low<=high){
            mid = (int)(low+high)/2;//2
            guess = nums[mid];
            if (guess==target){
                return mid;
                }
            if (guess > target){  
                high = mid-1;
                }
            else{
                low = mid+1;
                }
            }
        return high+1;
    }
};
