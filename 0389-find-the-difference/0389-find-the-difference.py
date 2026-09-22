class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascii_sum = sum(ord(char) for char in t) - sum(ord(char) for char in s)
        return chr(ascii_sum)
        # result=""
        # seen=set(s)
        # for char in t:
        #     if char in seen:
        #         seen.pop()
        #         continue
        #     else:
        #         result+=char
        # return result
