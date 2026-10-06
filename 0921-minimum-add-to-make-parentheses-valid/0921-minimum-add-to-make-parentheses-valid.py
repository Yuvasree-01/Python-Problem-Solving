class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for ch in s:
            if ch==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    count+=1
            else:
                stack.append(ch)
        return len(stack)+count
        # open_need=0
        # balance=0
        # for char in s:
        #     if char=='(':
        #         balance+=1
        #     else:
        #         balance-=1
        #     if balance<0:
        #         open_need+=1
        #         balance=0
        # return open_need+balance
