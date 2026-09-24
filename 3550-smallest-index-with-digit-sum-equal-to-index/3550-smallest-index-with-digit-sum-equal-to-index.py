from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            # Calculate the sum of the digits for the current number
            digit_sum = 0
            temp = val
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            # Since we iterate from 0 upwards, the first match is the smallest index
            if digit_sum == i:
                return i
                
        return -1

# from typing import List
# class Solution:
#     def smallestIndex(self, nums: List[int]) -> int:
#         sum=float('inf')
#         for i in range(len(nums)):
#             n=(nums[i]*(nums[i]+1))//2
#             print(n)
#             if n == i:
#                 if n<sum:
#                     sum=i
#         return sum if sum!=float('inf') else -1

