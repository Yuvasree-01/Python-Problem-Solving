class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_str = "1"
        
        # Generate terms from 2 up to n
        for _ in range(1, n):
            next_str = []
            i = 0
            
            # Group consecutive identical digits
            while i < len(current_str):
                count = 1
                # Increment count while adjacent digits match
                while i + 1 < len(current_str) and current_str[i] == current_str[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count and the digit character
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
                
            current_str = "".join(next_str)
            
        return current_str
