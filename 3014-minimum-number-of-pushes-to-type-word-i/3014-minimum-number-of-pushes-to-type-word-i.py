class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        
        for i in range(n):
            # i // 8 gives the layer: 
            # Indices 0-7   -> 0 (needs 1 push)
            # Indices 8-15  -> 1 (needs 2 pushes)
            # Indices 16-23 -> 2 (needs 3 pushes)
            # Indices 24-25 -> 3 (needs 4 pushes)
            total_pushes += (i // 8) + 1
            
        return total_pushes