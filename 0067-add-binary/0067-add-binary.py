class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Pointers starting at the end of both strings
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop as long as there are digits to process or a carry remaining
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add digit from string 'a' if available
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Add digit from string 'b' if available
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The current digit is total modulo 2 (removes the carry)
            result.append(str(total % 2))
            
            # Calculate the new carry (integer division by 2)
            carry = total // 2
            
        # Reverse the result list because we added digits from right to left
        return "".join(reversed(result))
