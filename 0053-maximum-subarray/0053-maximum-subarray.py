class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # else:
        #     max_sum=nums[0]
        #     curr_sum=nums[0]
        #     for num in nums[1:]:
        #         curr_sum = max(num,curr_sum+num)
        #         if curr_sum>max_sum:
        #             max_sum= curr_sum
        #     return max_sum
        
        current_sum=0
        max_sum=float('-inf')

        if not nums:
            return 0
        
        for current_element in nums:
            if current_element>current_sum+current_element:
                current_sum=current_element
            else:
                current_sum=current_sum+current_element
            if current_sum>max_sum:
                max_sum=current_sum
        return max_sum
        
        