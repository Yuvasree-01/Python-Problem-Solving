class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s=""
        # for i in range(0,len(digits)):
        #     s=s+str(digits[i])
        # num= int(s)+1
        # s=str(num)
        # i=0
        # result=[]
        # for i in range(0,len(s)):
        #     result.append(int(s[i]))
        #     print(result)
        # return result


        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits 
            
            digits[i] = 0
            
        return [1] + digits