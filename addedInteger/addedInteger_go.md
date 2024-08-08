func getMax(nums []int) int {
    n := len(nums)
    if n == 0{
        return 0
    }
    ans := nums[0]
    for _, num := range nums {
        ans = max(ans, num)
    }
    return ans
}

func addedInteger(nums1 []int, nums2 []int) int {
    return getMax(nums2) - getMax(nums1)
}