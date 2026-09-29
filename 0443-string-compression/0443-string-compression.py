class Solution:
    def compress(self, chars: list[str]) -> int:
        write_idx = 0
        read_idx = 0
        
        while read_idx < len(chars):
            char = chars[read_idx]
            count = 0
            
            # Count consecutive occurrences
            while read_idx < len(chars) and chars[read_idx] == char:
                read_idx += 1
                count += 1
            
            # Write the character
            chars[write_idx] = char
            write_idx += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1
                    
        return write_idx
