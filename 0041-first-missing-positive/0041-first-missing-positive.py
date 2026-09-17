class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # n = len(nums)
        
        # for i in range(n):
        #     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        #         correct_idx = nums[i] - 1
        #         nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1
        # return n + 1
        seen = set(nums)  
        n = len(nums)
        for i in range(1,n+1):
            if i not in seen:
                return i
                
        return n+1  