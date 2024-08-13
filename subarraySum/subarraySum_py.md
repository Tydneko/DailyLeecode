class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        pre, ans = 0, 0
        dic[0] = 1
        for num in nums:
            pre += num
            if pre - k in dic:
                ans += dic[pre-k]
            dic[pre] += 1
        return ans