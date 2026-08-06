class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case: if 0 rows are requested, return an empty list
        if numRows == 0:
            return []
            
        # Step 1: Initialize the triangle with the first row
        triangle = [[1]]
        
        # Step 2: Loop to build each row one by one from row index 1 to numRows-1
        for i in range(1, numRows):
            # Step 3: Fetch the row right above the current one
            prev_row = triangle[-1]
            
            # Step 4: Every row starts with a '1' boundary
            new_row = [1]
            
            # Sum up adjacent pairs from the previous row to fill inner cells
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
                
            # Every row ends with a '1' boundary
            new_row.append(1)
            
            # Step 5: Append the completed row to our master triangle list
            triangle.append(new_row)
            
        return triangle
