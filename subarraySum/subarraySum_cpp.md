class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        int pre = 0, ans = 0;
        mp[0] = 1;
        for(auto &e :nums){
            pre += e;
            if(mp.find(pre - k) != mp.end()){
                ans += mp[pre - k];
            }
            mp[pre]++;
        }
        return ans;
    }
};