class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to their Roman numeral equivalents in descending order
        roman_mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = []
        
        for value, symbol in roman_mapping:
            if num == 0:
                break
            # Find out how many times this symbol fits into the number
            count = num // value
            if count > 0:
                res.append(symbol * count)
                num %= value  # Keep the remainder
                
        return "".join(res)
