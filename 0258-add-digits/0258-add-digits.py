class Solution:
    def addDigits(self, num: int) -> int:
        # s= str(num)
        # if len(s)<=1:
        #     return num
        # temp=len(s)
        # add=len(s)

        # while len(str(add))>1:
        #     for i in range (0,len(temp)):
        #         add = int(s[i])+int(s[i+1])
        #         if len(str(add)) <=1:
        #             return add
        #         else:
        #             temp= len(add)
        # return add

        if num == 0:
            return 0
        # If a number is a multiple of 9, the repeated digital sum is always 9
        if num % 9 == 0:
            return 9
        # Otherwise, the result is simply the remainder
        return num % 9