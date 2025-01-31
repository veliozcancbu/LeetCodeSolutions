class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = defaultdict(int)
        def paint(r: int, c: int, color: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1: return
            grid[r][c] = color
            islands[color] += 1
            for dx, dy in directions:
                x = dx + r
                y = dy + c
                paint(x, y, color)


        color = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                paint(i, j, color)
                color += 1
        
        maxArea = 0
        if islands:
            maxArea = max(islands.values())
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0: continue
                colors = set()
                for dx, dy in directions:
                    x = dx + i
                    y = dy + j
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0: continue
                    colors.add(grid[x][y])
                area = 1
                for color in colors:
                    area += islands[color]
                maxArea = max(maxArea, area)
        return maxArea

  """
  You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.

"""
