class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # INT_MAX = 2**31 - 1
        # INT_MIN = -2**31
        # if dividend == INT_MIN and divisor == -1:
        #     return INT_MAX

        # negative = (dividend < 0) ^ (divisor < 0)
        # dividend, divisor = abs(dividend), abs(divisor)
        # quotient = 0
        
        # while dividend >= divisor:
        #     temp_divisor = divisor
        #     multiple = 1
            
        #     while dividend >= (temp_divisor << 1):
        #         temp_divisor <<= 1
        #         multiple <<= 1

        #     dividend -= temp_divisor
        #     quotient += multiple
            
        # return -quotient if negative else quotient

        negative = (dividend < 0) != (divisor < 0)

        divisor = abs(divisor)
        dividend = abs(dividend)

        quotient = 0 
        while dividend >= divisor:
            current = divisor
            multiple = 1
            while dividend >= current + current:
                current += current
                multiple += multiple
            dividend -= current
            quotient += multiple
        if negative:
            quotient = -quotient
        if quotient > 2**31 - 1:
            return 2**31 - 1
        if quotient < -2**31:
            return -2**31
        return quotient