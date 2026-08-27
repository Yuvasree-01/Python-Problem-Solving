class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base case: if rows equal 1 or string is short, no pattern change occurs
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Create a list of strings to represent each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            # Turn around when we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down based on direction
            current_row += 1 if going_down else -1
            
        # Combine all rows together to get the final answer
        return "".join(rows)
