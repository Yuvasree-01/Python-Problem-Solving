class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # The first number can at most take up half the string length
        for i in range(1, n // 2 + 1):
            # Leading zero check for the first number
            if num[0] == '0' and i > 1:
                break
                
            # The second number must leave enough space for the third number
            for j in range(i + 1, n):
                # Leading zero check for the second number
                if num[i] == '0' and j - i > 1:
                    break
                
                # Extract the first two numbers as integers
                num1 = int(num[0:i])
                num2 = int(num[i:j])
                
                # Start tracking the remaining part of the string
                k = j
                while k < n:
                    # Calculate what the next expected number should be
                    next_num = num1 + num2
                    next_str = str(next_num)
                    
                    # Check if the remaining string starts with our expected sum
                    if not num.startswith(next_str, k):
                        break
                    
                    # Slide the window forward
                    k += len(next_str)
                    num1, num2 = num2, next_num
                
                # If we successfully consumed the entire string, it's valid!
                if k == n:
                    return True
                    
        return False
