func subarraySum(nums []int, k int) int {
    mp := map[int]int{}
    pre, ans := 0, 0
    mp[0] = 1
    for i := 0; i < len(nums); i++{
        pre += nums[i]
        if val, ok := mp[pre - k];ok{
            ans += val
        }
        mp[pre] += 1
    }
    return ans
}