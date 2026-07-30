class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        
        if len(unique_nums) < 3:
            return max(unique_nums)
            
        # Remove the 1st max and 2nd max
        unique_nums.remove(max(unique_nums))
        unique_nums.remove(max(unique_nums))
        
        # The next maximum is the 3rd maximum
        return max(unique_nums)  