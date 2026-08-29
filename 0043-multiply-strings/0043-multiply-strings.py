class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        # The product of two numbers of lengths N and M can at most have N + M digits
        result = [0] * (len(num1) + len(num2))
        
        # Loop backwards through both string inputs
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Convert characters to digits using ASCII distance
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Multiply digits and add to the existing value at this position
                mul = digit1 * digit2
                p1 = i + j
                p2 = i + j + 1
                
                total = mul + result[p2]
                
                # Store the remainder in the current position, carry goes to position p1
                result[p2] = total % 10
                result[p1] += total // 10
                
        # Convert the integer array back to strings, skipping leading zeros
        start_index = 0
        while start_index < len(result) and result[start_index] == 0:
            start_index += 1
            
        return "".join(str(digit) for digit in result[start_index:])