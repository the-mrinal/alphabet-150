class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i,j):
            stack = [(i,j)]
            isClosedIsland = True
            grid[i][j] = 1
            while stack:
                x,y = stack.pop()
                
                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    n_a = a + x
                    n_b = b + y
                    
                    if n_a < 0 or n_a >= m or n_b < 0 or n_b >= n:
                        isClosedIsland = False
                        continue
                        
                    if grid[n_a][n_b] == 1:
                        continue
                    grid[n_a][n_b] = 1
                    stack.append((n_a,n_b))
                
            return 1 if isClosedIsland else 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += dfs(i,j)
        
        return count