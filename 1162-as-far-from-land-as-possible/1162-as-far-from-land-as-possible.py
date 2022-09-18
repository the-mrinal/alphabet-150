class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        que = deque()
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    que.append([i,j,0])
        
        maxDepth = -1
        
        while que:
            x,y,d = que.popleft()
            
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                n_a = a + x
                n_b = b + y
                
                if n_a < 0 or n_a >= n or n_b < 0 or n_b >= n or grid[n_a][n_b] == 1:
                    continue
                
                grid[n_a][n_b] = 1
                maxDepth = max(maxDepth,d + 1)
                que.append([n_a,n_b,d + 1])
        
        return maxDepth