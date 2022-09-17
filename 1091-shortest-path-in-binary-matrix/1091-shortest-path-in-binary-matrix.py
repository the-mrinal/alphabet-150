class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        que = deque()
        n = len(grid)
        directions = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        visited = set()
        if grid and grid[0][0] == 0:
            que.append([0,0,1])
            visited.add((0,0))
        
        while que:
            x,y,path = que.popleft()
            
            if x == n - 1 and y == n - 1:
                return path
            
            for a,b in directions:
                n_a = a + x
                n_b = b + y
                
                if n_a < 0 or n_a >= n or n_b < 0 or n_b >= n or (n_a,n_b) in visited or grid[n_a][n_b] == 1:
                    continue
                que.append([n_a,n_b,path + 1])
                visited.add((n_a,n_b))
        
        return -1