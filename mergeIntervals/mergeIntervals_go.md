func merge(intervals [][]int) [][]int {
    slices.SortFunc(intervals, func(i, j []int)int{ return i[0] - j[0]})
    var ans [][]int

    for _, v := range intervals{
        n := len(ans)
        if n == 0 || ans[n-1][1] < v[0]{
            ans = append(ans, v)
        }else{
            ans[n-1][1] = max(ans[n-1][1], v[1])
        }
    }
    return ans
}