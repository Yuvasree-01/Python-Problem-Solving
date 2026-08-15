# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
        # row1="qwertyuiop"
        # row2="asdfghjkl"
        # row3="zxcvbnm"
        # sorted(row1)
        # sorted(row1)
        # sorted(row1)

        # result=[]
        # for word in words:
        #     word=sorted(word)
        #     # word.lower()
        #     if words[word] in row1:
        #         result.append(words[word])
        #         print(word)
        #     elif word in row2:
        #         result.append(words[word])
        #     elif word in row3:
        #         result.append(words[word])
        #     else:
        #         continue
        # return result


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Convert rows into sets of lowercase characters for O(1) lookups
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            word_set = set(word.lower())
            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                result.append(word)
                
        return result
