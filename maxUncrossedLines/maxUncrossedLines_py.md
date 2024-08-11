class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(n - 1, m - 1)


# '@cache' 为python3中的缓存装饰器，可以通过利用缓存来存储函数的计算结果，以便在下次调用相同输入参数的时候能够直接返回缓存中的结果，而不需要重新执行函数逻辑。