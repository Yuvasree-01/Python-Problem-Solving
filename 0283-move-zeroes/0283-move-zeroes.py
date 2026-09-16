class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                count+=1
                nums.pop(i)

        if count>0:
            nums[:]= nums + [0]*count
