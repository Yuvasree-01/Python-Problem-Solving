class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 3:
            return n
            
        one_step_before = 2  # ways(2)
        two_steps_before = 1 # ways(1)
        all_ways = 0
        
        for i in range(3, n + 1):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways
            
        return all_ways
