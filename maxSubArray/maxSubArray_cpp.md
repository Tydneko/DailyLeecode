class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre_sum = 0, max_sum = INT_MIN;
        for(int i = 0; i < nums.size(); ++i){
            if(pre_sum < 0){
                max_sum = max(max_sum, nums[i]);
                pre_sum = nums[i];
            }else{
                pre_sum += nums[i];
                max_sum = max(max_sum, pre_sum);
            }
        }
        return max_sum;
    }
};