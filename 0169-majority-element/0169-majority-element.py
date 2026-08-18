class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # Pick a new candidate if counter drops to zero
            if count == 0:
                candidate = num
                
            # Adjust the counter based on character match
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate