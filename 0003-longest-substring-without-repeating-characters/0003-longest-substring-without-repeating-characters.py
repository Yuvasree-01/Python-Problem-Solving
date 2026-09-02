class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_set = set()
        left=0
        max_len=1

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[right])
            max_len = max(len(char_set),max_len)
        return max_len