class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #method 1:
        # if word.isupper() or word.islower() or (word[0:1].isupper() and word[1:].islower()):
        #     return True
        # return False 

        # method 2:
        return word.islower() or word.isupper() or word.istitle()