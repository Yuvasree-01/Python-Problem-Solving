class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        for char in columnTitle:
            # Convert character to its 1-based numerical value ('A' -> 1, 'B' -> 2...)
            # ord('A') is 65. Subtracting 64 maps 'A' to 1.
            current_value = ord(char) - 64
            
            # Shift the existing result to the left by a power of 26, then add the new value
            result = result * 26 + current_value
            
        return result