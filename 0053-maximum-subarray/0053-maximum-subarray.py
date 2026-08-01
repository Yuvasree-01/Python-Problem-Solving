class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            max_sum=nums[0]
            curr_sum=nums[0]
            for num in nums[1:]:
                curr_sum = max(num,curr_sum+num)
                if curr_sum>max_sum:
                    max_sum= curr_sum
            return max_sum
        