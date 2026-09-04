class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[]
        product=1
        zero=0
        for num in nums:
            if num==0:
                zero+=1
            else:
                product*=num
        for i in nums:
            if zero==0:
                prod.append(int(product/i))
            elif i==0 and zero==1:
                prod.append(int(product))
            elif i!=0 and zero>=1:
                prod.append(0)
            else:
                prod.append(0)
        return prod