class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # ascii_sum = sum(ord(char) for char in t) - sum(ord(char) for char in s)
        # return chr(ascii_sum)
        diff = Counter(t) - Counter(s)
        
        # Get the single remaining character key
        return list(diff.keys())[0]
