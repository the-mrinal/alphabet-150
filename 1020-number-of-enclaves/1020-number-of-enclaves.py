class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        totalCount = 0
        visited = set()
        
        m = len(grid)
        n = len(grid[0])
        
        def countIsland(x,y):
            stack = []
            
            visited.add((x,y))
            
            stack.append((x,y))
            
            count = 0
            
            out = False
            
            while stack:
                x,y = stack.pop()
                count += 1
                
                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    n_a = a + x
                    n_b = b + y
                    if n_a < 0 or n_a >= m or n_b < 0 or n_b >= n:
                        out = True
                        continue
                    if grid[n_a][n_b] == 0 or (n_a,n_b) in visited:
                        continue
                    stack.append((n_a,n_b))
                    visited.add((n_a,n_b))
            
            if out:
                return 0
            return count
                                
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    totalCount += countIsland(i,j)
        
        return totalCount