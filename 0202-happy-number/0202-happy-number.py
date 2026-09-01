# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def recursive(s):
#             temp=0
#             for char in s:
#                 temp+=int(char)**2
#                 print(temp)
#             s+=str(temp)
#             return s
#         s=str(n)
#         if len(s)==1 and s[0]=='1':
#             return True
#         else:
#             return recursive(s)
#         return False

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            # If we see the number again, we are in an infinite loop
            if n in seen:
                return False
            
            seen.add(n)
            
            # Calculate the sum of the squares of digits
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10
                
            n = total_sum
            
        return True
