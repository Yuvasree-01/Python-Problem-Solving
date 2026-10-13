import numpy as np
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = np.square(np.array(nums, dtype=np.int64))
        h = len(nums) // 2
        return int(sq.sum() - 2 * np.partition(sq, h)[:h].sum()) 
        # n = len(nums)
        # for i in range(n):
        #     nums[i] *= nums[i]
        # nums.sort()
        # return -sum(nums[: n // 2]) + sum(nums[n // 2 :])