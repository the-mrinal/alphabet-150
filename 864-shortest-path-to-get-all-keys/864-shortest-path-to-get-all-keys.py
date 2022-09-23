class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        moveCost = float('inf')

        startPoint = None
        totalKeys = [0]*6

        m = len(grid)
        n = len(grid[0])

        def scanPlayground():
            nonlocal startPoint,totalKeys
            keyCount = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j].islower():
                        totalKeys[ord(grid[i][j]) - ord('a')] = 1
                    if grid[i][j] == '@':
                        startPoint = (i,j)


        scanPlayground()
        totalKeys = tuple(totalKeys)

        # print(startPoint)
        stack = [(startPoint[0],startPoint[1],tuple([0]*6))]
        visited = {(startPoint[0],startPoint[1],tuple([0]*6))}
        depth = 0
        
        while stack:
            new_stack = []
            
            for x,y,keys in stack:
                for a,b in directions:
                    n_a = x + a
                    n_b = y + b
                    if n_a >=0 and n_a < m and n_b >= 0 and n_b < n and grid[n_a][n_b] != '#':
                        val = grid[n_a][n_b]
                        if val in '.@':
                            if (n_a,n_b,keys) not in visited:
                                new_stack.append((n_a,n_b,keys))
                                visited.add((n_a,n_b,keys))
                        elif val.islower():
                            new_keys = list(keys)
                            new_keys [ord(val) - ord('a')] = 1
                            new_keys = tuple(new_keys)
                            if new_keys == totalKeys:
                                return depth + 1
                            if (n_a,n_b,new_keys) not in visited:
                                new_stack.append((n_a,n_b,new_keys))
                                visited.add((n_a,n_b,new_keys))
                        else:
                            if keys[ord(val.lower()) - ord('a')] == 1 and (n_a,n_b,keys) not in visited:
                                new_stack.append((n_a,n_b,keys))
                                visited.add((n_a,n_b,keys))
            depth += 1
            stack = new_stack
        return -1
        
        
        
        
        
        
        
        
        
        
        
        