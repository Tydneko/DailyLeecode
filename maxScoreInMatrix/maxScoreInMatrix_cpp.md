class Solution {
public:
    int maxScore(std::vector<std::vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int ans = INT_MIN;
    vector<vector<int>> dp (m+1, vector(n+1, INT_MAX));
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            int cur_min = min(dp[i+1][j], dp[i][j+1]);
            ans = max(ans, grid[i][j] - cur_min);
            dp[i+1][j+1] = min(cur_min, grid[i][j]);
        }
    }
    return ans;
}
};