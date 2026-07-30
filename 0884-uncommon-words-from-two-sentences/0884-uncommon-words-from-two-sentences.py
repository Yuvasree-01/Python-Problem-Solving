class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count=Counter(s1.split()+s2.split())
        result=[]
        for word,count in word_count.items():
            if count == 1:
                result.append(word)
        return result

