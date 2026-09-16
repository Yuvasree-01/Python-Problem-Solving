class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count=0
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i]==0:
        #         count+=1
        #         nums.pop(i)

        # if count>0:
        #     nums[:]= nums + [0]*count
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums