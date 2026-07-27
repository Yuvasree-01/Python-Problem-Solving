class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result=[]
        count=[]
        for num in nums:
            if num==0:
                count.append(0)
            else:
                result.append(num)
                
        nums[:]= result+count