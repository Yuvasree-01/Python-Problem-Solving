class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # result=False
        # count=0
        # temp=nums[0]
        # for i in range(0,len(nums)-1):
        #     if nums[i]<temp:
        #         temp=nums[i]
        #     if temp<nums[i+1]:
        #         count+=1
        # if count>=3:
        #     return True
        # return result

        min1=min2=float("inf")
        for n in nums:
            if n<=min1:
                min1=n
            elif n<=min2:
                min2=n
            else:
                return True
        return False