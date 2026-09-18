class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # right=len(nums)-1
        # for left in range(0,right):
        #     if nums[left]==nums[right]:
        #         if abs(left-right)<=k:
        #             return True
                
        # return False
        
        window = set()
        
        for i in range(len(nums)):
            # If the number is already in our window, we found a nearby duplicate
            if nums[i] in window:
                return True
            
            # Add the current number to the window
            window.add(nums[i])
            
            # If the window size exceeds k, remove the oldest element
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False
