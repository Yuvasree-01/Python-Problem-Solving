class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
            
        remainder = 0
        
        # Step 2: Loop from length 1 up to k
        for length in range(1, k + 1):
            # Step 3: Shift the previous remainder left and add 1
            remainder = (remainder * 10 + 1) % k
            
            # Step 4: If it divides evenly, we found our smallest length
            if remainder == 0:
                return length
                
        # Fallback if no solution is found within k steps
        return -1