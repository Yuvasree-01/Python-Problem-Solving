class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red=[]
        # white=[]
        # blue=[]
        # for i in range(0,len(nums)):
        #     if nums[i]==0:
        #         red.append(0)
        #     elif nums[i]==1:
        #         white.append(1)
        #     else:
        #         blue.append(2)
        # result=red+white+blue
        # nums[:]=result

        # Pass 1: Count the occurrences of each color
        c0 = nums.count(0)
        c1 = nums.count(1)
        
        # Pass 2: Overwrite the array sequentially based on counts
        for i in range(len(nums)):
            if i < c0:
                nums[i] = 0
            elif i < c0 + c1:
                nums[i] = 1
            else:
                nums[i] = 2
