class Solution:
    def reverseBits(self, n: int) -> int:
        # result = 0
        # for _ in range(32):
        #     result <<= 1
            
        #     # Extract the rightmost bit of n and add it to result
        #     result |= (n & 1)
            
        #     # Shift n right to process the next bit in line
        #     n >>= 1
            
        # return result
        
        # ans = 0
        # for _ in range(32):
        #     bit = n & 1
        #     ans = (ans << 1) | bit
        #     n >>= 1
        # return ans

        # 1. Swap odd and even bits (groups of 1)
        # 0x55555555 is 01010101... in binary
        # 0xAAAAAAAA is 10101010... in binary
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)
        
        # 2. Swap adjacent pairs (groups of 2)
        # 0x33333333 is 00110011... in binary
        # 0xCCCCCCCC is 11001100... in binary
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)
        
        # 3. Swap adjacent nibbles (groups of 4)
        # 0x0F0F0F0F is 00001111... in binary
        # 0xF0F0F0F0 is 11110000... in binary
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)
        
        # 4. Swap adjacent bytes (groups of 8)
        # 0x00FF00FF is 8 zeros, 8 ones...
        # 0xFF00FF00 is 8 ones, 8 zeros...
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)
        
        # 5. Swap the left and right 16-bit halves
        # Mask with 0xFFFFFFFF at the end to keep it bounded to 32 bits in Python
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        
        return n & 0xFFFFFFFF

