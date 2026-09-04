class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Non division method:
        left=[]
        left_product=1
        right_product=1
        for i in range(len(nums)):
            left.append(left_product)
            left_product=left_product*nums[i]
        for j in range(len(nums)-1,-1,-1):
            left[j]=left[j]* right_product
            right_product=nums[j]*right_product
        return left
            


        #Division method:

        # prod=[]
        # product=1
        # zero=0
        # for num in nums:
        #     if num==0:
        #         zero+=1
        #     else:
        #         product*=num
        # for i in nums:
        #     if zero==0:
        #         prod.append(int(product/i))
        #     elif i==0 and zero==1:
        #         prod.append(int(product))
        #     elif i!=0 and zero>=1:
        #         prod.append(0)
        #     else:
        #         prod.append(0)
        # return prod