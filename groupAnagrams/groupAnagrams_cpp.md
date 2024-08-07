class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> ump;

        for(auto &s: strs){
            string key = s;
            sort(key.begin(), key.end());
            ump[key].emplace_back(s);
        }

        vector<vector<string>> ans;
        int i = 0;
        for(auto &e: ump){
            ans.emplace_back(e.second);
        }
        return ans;
    }
};