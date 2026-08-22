# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         result = []
#         carry = 0
        
#         i = len(num1) - 1
#         j = len(num2) - 1
        
#         while i >= 0 or j >= 0 or carry:
#             digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
#             digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
#             column_sum = digit1 + digit2 + carry
            
#             carry = column_sum // 10
#             result.append(str(column_sum % 10))
            
#             i -= 1
#             j -= 1
            
#         return "".join(reversed(result))
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # Helper function to perform recursive column addition
        def add_helper(i: int, j: int, carry: int) -> str:
            # Base case: if we ran out of digits and there is no carry, stop
            if i < 0 and j < 0 and not carry:
                return ""
            
            # Extract current digits using ASCII offset (ord)
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # Compute total for the current position
            total = digit1 + digit2 + carry
            
            # Recursive call moves leftward, calculating the next position's carry
            # The result of the next columns is placed BEFORE the current column's digit
            return add_helper(i - 1, j - 1, total // 10) + str(total % 10)
        
        # Start recursion from the far-right index of both strings
        return add_helper(len(num1) - 1, len(num2) - 1, 0)
