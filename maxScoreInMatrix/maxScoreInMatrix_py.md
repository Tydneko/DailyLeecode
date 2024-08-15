class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        ans = -inf
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                cur = min(dp[i+1][j], dp[i][j+1])
                ans = max(ans, x - cur)
                dp[i+1][j+1] = min(cur, x)
        return ans
