class Solution:
    def countCommas(self, n: int) -> int:
        # print(len(str(n)))
        # num=len(str(n))
        t=1000
        res=0
        # if num<4:
        #     return res
        # elif num==4 or num==5:
        #     return n%t+1
        # elif num==6:
        #     return n-t+1
        while t<=n:
            res += n-t+1
            t*=1000
        return res
