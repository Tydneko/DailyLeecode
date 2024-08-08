func maxSubArray(nums []int) int {
    pre_sum := 0
    max_sum := -2147483648
    for i := 0; i < len(nums); i++{
        if pre_sum < 0{
            max_sum = max(max_sum, nums[i])
            pre_sum = nums[i]
        }else{
            pre_sum += nums[i]
            max_sum = max(max_sum, pre_sum)
        }
    }
    return max_sum
}