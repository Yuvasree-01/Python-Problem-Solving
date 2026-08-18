class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Shift 1-based indexing to 0-based indexing
            columnNumber -= 1
            
            # Find the remainder to isolate the current character code (0 to 25)
            remainder = columnNumber % 26
            
            # ord('A') is 65. Adding the remainder gives us the correct character
            char = chr(65 + remainder)
            result.append(char)
            
            # Divide by 26 to move to the next position on the left
            columnNumber //= 26
            
        # Since we calculated digits from right to left, reverse the result
        return "".join(reversed(result))