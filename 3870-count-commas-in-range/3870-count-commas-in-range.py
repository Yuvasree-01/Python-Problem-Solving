class Solution:
    def countCommas(self, n: int) -> int:
        t=1000
        res=0
        while t<=n:
            res += n-t+1
            t*=1000
        return res