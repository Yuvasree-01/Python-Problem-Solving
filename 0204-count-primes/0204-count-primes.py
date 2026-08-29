class Solution:
    mx=5*(10**6)+1
    p=[True]*mx
    p[0]=p[1]=False
    idx=2
    while idx*idx<=mx:
        if p[idx]==True:
            for i in range(idx*idx,mx,idx):
                p[i]=False
        idx+=1
        
    pref=[0]*mx
    for i in range(2,mx):
        pref[i]=pref[i-1]+ (1 if p[i-1]==True else 0)
    
    def countPrimes(self, n: int) -> int:
        return self.pref[n]