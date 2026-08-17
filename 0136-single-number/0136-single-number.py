class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Counter creates a frequency map of the list automatically
        counts = Counter(nums)
        
        # Look for the number with a count/frequency of 1
        for num, count in counts.items():
            if count == 1:
                return num