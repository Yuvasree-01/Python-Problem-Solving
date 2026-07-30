class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_count=Counter(arr)
        freq_count=set()
        for num,count in unique_count.items():
            if count not in freq_count:
                freq_count.add(count)
            else:
                return False
        return True