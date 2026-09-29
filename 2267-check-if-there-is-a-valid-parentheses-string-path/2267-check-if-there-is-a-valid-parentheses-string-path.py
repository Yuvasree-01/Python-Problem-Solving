# from collections import deque
# class Solution:
#     def hasValidPath(self, grid: list[list[str]]) -> bool:
#         m, n = len(grid), len(grid[0])

#         # Total path length must be even
#         if (m + n - 1) % 2 != 0:
#             return False

#         # First character must be '('
#         if grid[0][0] == ')':
#             return False

#         # queue stores (row, col, balance)
#         queue = deque()
from functools import cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Quick boundary checks
        if (m + n - 1) % 2 == 1 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        @cache
        def dfs(i: int, j: int, k: int) -> bool:
            # Update balance based on current cell
            k += 1 if grid[i][j] == '(' else -1
            
            # Prune invalid paths
            if k < 0 or k > m - i + n - j - 1:
                return False
                
            # Base case: reached bottom-right cell
            if i == m - 1 and j == n - 1:
                return k == 0
                
            # Move down or right
            res = False
            if i + 1 < m:
                res = res or dfs(i + 1, j, k)
            if not res and j + 1 < n:
                res = res or dfs(i, j + 1, k)
                
            return res

        return dfs(0, 0, 0)
#         queue.append((0, 0, 1))

#         # visited[row][col][balance]
#         visited = [[[False] * (m + n) for _ in range(n)] for _ in range(m)]
#         visited[0][0][1] = True

#         directions = [(1, 0), (0, 1)]  # down, right

#         while queue:
#             row, col, balance = queue.popleft()

#             # Reached destination
#             if row == m - 1 and col == n - 1:
#                 if balance == 0:
#                     return True

#             for dr, dc in directions:
#                 newRow, newCol = row + dr, col + dc

#                 # Out of bounds
#                 if newRow >= m or newCol >= n:
#                     continue

#                 newBalance = balance + 1 if grid[newRow][newCol] == '(' else balance - 1

#                 # Invalid prefix
#                 if newBalance < 0:
#                     continue

#                 # Already visited same state
#                 if visited[newRow][newCol][newBalance]:
#                     continue

#                 visited[newRow][newCol][newBalance] = True
#                 queue.append((newRow, newCol, newBalance))

#         return False
