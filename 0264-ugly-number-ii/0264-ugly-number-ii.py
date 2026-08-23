class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1 # The first ugly number is always 1
        
        # Pointers for the multiples of 2, 3, and 5
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            # Calculate the next potential candidate for each prime factor
            next_2 = ugly[p2] * 2
            next_3 = ugly[p3] * 3
            next_4 = ugly[p5] * 5  # Note: conceptually multiplying by 5
            
            # Select the smallest next candidate
            current_ugly = min(next_2, next_3, next_4)
            ugly[i] = current_ugly
            
            # Move pointers forward if their calculated value matches the chosen minimum
            if current_ugly == next_2:
                p2 += 1
            if current_ugly == next_3:
                p3 += 1
            if current_ugly == next_4:
                p5 += 1
                
        return ugly[-1]