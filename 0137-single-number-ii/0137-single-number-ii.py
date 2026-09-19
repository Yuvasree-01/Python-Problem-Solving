class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
        # ones = 0
        # twos = 0
        
        # for num in nums:
        #     twos ^= (ones & num)
        #     ones ^= num
        
        #     three_times = ~(ones & twos)
            
        #     ones &= three_times
        #     twos &= three_times
            
        # return ones
