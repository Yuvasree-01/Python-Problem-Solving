class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current_path: list[int], remaining_target: int):
            if remaining_target == 0:
                result.append(list(current_path))
                return
            if remaining_target < 0:
                return
            
            for i in range(start, len(candidates)):
                current_path.append(candidates[i])
                # Allow reuse of the same element by passing 'i' instead of 'i + 1'
                backtrack(i, current_path, remaining_target - candidates[i])
                current_path.pop()
                
        backtrack(0, [], target)
        return result