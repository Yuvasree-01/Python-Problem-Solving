class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                distinct = len(seen)
                ans = ans + (distinct*distinct)
        return ans
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     s = set()
        #     for j in range(i, n):
        #         s.add(nums[j])
        #         res += len(s) * len(s)
        # return res