class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_str: str, open_count: int, close_count: int):
            # Base Case: If the string reaches the target length, save it
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Choice 1: Add an opening parenthesis
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Choice 2: Add a closing parenthesis
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        # Start the recursive chain with an empty string
        backtrack("", 0, 0)
        return result