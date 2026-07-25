class Solution:
    def toLowerCase(self, s: str) -> str:
        result = "".join(char.lower() for char in s )
        return result