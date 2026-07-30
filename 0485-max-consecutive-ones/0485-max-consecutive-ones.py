class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # current_freq =0
        # max_freq=0
        # for i in range(len(nums)):
        #     if nums[i]==1:
        #         current_freq += 1
        #         if current_freq > max_freq:
        #             max_freq = current_freq
        #     else:
        #         current_freq = 0
        # return max_freq

        i = j = 0
        for num in nums:
            if num == 1:
                i += 1
            else:
                j = max(i,j)
                i = 0
        return max(i,j)