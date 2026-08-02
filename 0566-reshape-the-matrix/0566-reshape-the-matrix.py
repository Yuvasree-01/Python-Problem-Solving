class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
            
        flat_list = [element for row in mat for element in row]
        
        reshaped_matrix = [flat_list[i : i + c] for i in range(0, len(flat_list), c)]
        
        return reshaped_matrix