class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum, max_sum = 0, -2147483648
        for num in nums:
            if pre_sum < 0:
                max_sum = max(max_sum, num)
                pre_sum = num
            else:
                pre_sum += num
                max_sum = max(max_sum, pre_sum)
        return max_sum