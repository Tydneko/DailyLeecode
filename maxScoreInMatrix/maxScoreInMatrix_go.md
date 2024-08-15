func maxScore(grid [][]int) int {
    ans := math.MinInt
    m, n := len(grid), len(grid[0])
    dp := make([][]int, m + 1)
    dp[0] = make([]int, n + 1)
    for i := range dp[0]{
        dp[0][i] = math.MaxInt
    }

    for i, row := range grid{
        dp[i + 1] = make([]int, n + 1)
        dp[i + 1][0] = math.MaxInt
        for j, x := range row{
            cur := min(dp[i + 1][j], dp[i][j + 1])
            ans = max(ans, x - cur)
            dp[i + 1][j + 1] = min(cur, x)
        }
    }
    return ans
}