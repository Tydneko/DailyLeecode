func maxUncrossedLines(nums1 []int, nums2 []int) int {
    n, m := len(nums1), len(nums2)
    memo := make([][]int, n)
    for i := range memo{
        memo[i] = make([]int, m)
        for j := range memo[i]{
            memo[i][j] = -1
        }
    }

    var dfs func(int, int) int
    dfs = func(i, j int) int{
        if i < 0 || j < 0{
            return 0
        }
        p := &memo[i][j]
        if *p != -1{
            return *p
        }
        if nums1[i] == nums2[j]{
            *p = dfs(i - 1, j - 1) + 1
            return *p
        }
        *p = max(dfs(i - 1, j), dfs(i, j - 1))
        return *p
    }
    return dfs(n - 1, m - 1)
}