class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # result = []
        
        # for num in range(left, right + 1):
        #     if all(digit != '0' and num % int(digit) == 0 for digit in str(num)):
        #         result.append(num)
                
        # return result
        ans = []
        for i in range(left, right+1):
            num = i
            while num > 0:
                digit = num % 10
                if digit == 0 or i % digit != 0:
                    break
                num //= 10
            else:
                ans.append(i)
        
        return ans