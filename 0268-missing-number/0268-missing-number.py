class Solution:
    def missingNumber(self, nums: List[int]) -> int:
# method 1:
        # nums=sorted(nums)
        n=len(nums)
        # sum=0
        # og_sum=0

        # for i in range(n):
        #     sum+=nums[i]
        #     og_sum+=i
        # og_sum+=n
        # return og_sum-sum
        
# Method 2:
        expected = (n*(n+1))//2
        actual = sum(nums)
        return expected-actual