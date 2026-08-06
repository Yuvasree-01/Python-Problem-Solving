class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Step 1: Precompute factorials up to n-1 to determine bucket sizes
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        # Step 2: Create our available pool of digits
        # For n=4, numbers = ['1', '2', '3', '4']
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Step 3: Shift k to 0-based index for correct integer division mapping
        k -= 1
        result = []
        
        # Step 4: Step-by-step math elimination
        for i in range(n - 1, -1, -1):
            # Find the size of the current block
            block_size = factorials[i]
            
            # Identify which index in our numbers pool is the winner
            index = k // block_size
            
            # Remove that digit from the pool and add it to our result list
            result.append(numbers.pop(index))
            
            # Reduce k to its relative position inside the chosen block
            k %= block_size
            
        return "".join(result)
