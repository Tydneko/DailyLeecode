class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                cur_streak = 1

                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_streak += 1
                
                longest_streak = max(longest_streak, cur_streak)
                
        return longest_streak