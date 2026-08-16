class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        for i in range(0,len(nums)):
            mid = (left + right)//2
            if nums[mid]==target:
                return mid
            # if nums[left]==target:
            #     return left
            # if nums[right]==target:
            #     return right
            
            elif nums[mid]<target:
                left=mid+1
            else :
                right=mid-1
            
        return left
            
