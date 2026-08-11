class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,
            'V' :5,
            'X' :10,
            'L' :50,
            'C' :100,
            'D' :500,
            'M' :1000 }
        total = 0
        n = len(s)
        
        # 3. Use a range loop so we can look ahead at the next character
        for i in range(n):
            # If the current value is less than the next value, subtract it!
            if i + 1 < n and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                # Otherwise, add it safely
                total += roman[s[i]]
                
        return total