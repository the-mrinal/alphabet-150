class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque()
        visited = set()
        
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append([i,j,0])
                    visited.add((i,j))
        res = [[float('inf') for _ in range(n)]for _ in range(m)]

        while que:
            x,y,d = que.popleft()
            res[x][y] = d
            
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                n_a = a + x
                n_b = b + y
                
                if n_a >= m or n_a < 0 or n_b < 0 or n_b >= n or (n_a,n_b) in visited:
                    continue
                
                que.append([n_a,n_b,d + 1])
                visited.add((n_a,n_b))
            
        return res