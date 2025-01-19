class Solution:
    def trapRainWater(self, M):
        if not M or not M[0]: return 0
        r, c = len(M), len(M[0])
        if r < 3 or c < 3: return 0
        V = [[False]*c for _ in range(r)]
        H = []  

        def push(x):
            H.append(x)
            i = len(H) - 1
            p = (i - 1) // 2
            while i > 0 and H[i][0] < H[p][0]:
                H[i], H[p] = H[p], H[i]
                i = p
                p = (i - 1) // 2

        def pop():
            if not H: return None
            H[0], H[-1] = H[-1], H[0]
            top = H.pop()
            i, nH = 0, len(H)
            while True:
                l, r_ = 2*i+1, 2*i+2
                s = i
                if l < nH and H[l][0] < H[s][0]: s = l
                if r_ < nH and H[r_][0] < H[s][0]: s = r_
                if s == i: break
                H[i], H[s] = H[s], H[i]
                i = s
            return top

        for i in range(r):
            push((M[i][0], i, 0));       V[i][0] = True
            push((M[i][c-1], i, c-1));  V[i][c-1] = True
        for j in range(c):
            push((M[0][j], 0, j));       V[0][j] = True
            push((M[r-1][j], r-1, j));   V[r-1][j] = True

        ans = 0
        D = [(1,0), (-1,0), (0,1), (0,-1)]
  
        while H:
            h, x, y = pop()
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and not V[nx][ny]:
                    V[nx][ny] = True
                    if M[nx][ny] < h:
                        ans += h - M[nx][ny]
                        push((h, nx, ny))
                    else:
                        push((M[nx][ny], nx, ny))
        return ans


"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""
