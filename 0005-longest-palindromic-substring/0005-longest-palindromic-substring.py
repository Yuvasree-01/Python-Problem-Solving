class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""

        
        # lead=0
        # rear=-1
        # n=len(s)-1
        # result=""
        # for char in range(1,n):
        #     if s[lead]==s[rear]:
        #         if s[char]== s[n-rear]:
        #             result.append(s[lead])
        #             result.append(s[char])
        #             result.append(s[n-rear])
        #             result.append(rear)
        #         else:
        #             result.pop()
            
        #     lead+=1
        #     rear-=1
        # return result
