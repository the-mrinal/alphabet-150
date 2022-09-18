class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        adjMap = defaultdict(list)
        
        for a,b in redEdges:
            adjMap[a].append([b,'R'])
        
        for a,b in blueEdges:
            adjMap[a].append([b,'B'])
        
        que = deque()
        
        
        redAns = [0] + [float('inf')]*(n - 1)
        blueAns = [0] + [float('inf')]*(n - 1)
        
        for child in adjMap[0]:
            val,C =  child
            if val != 0:
                que.append(child + [1])
                if C == 'R':
                    redAns[val] = 1
                else:
                    blueAns[val] = 1
        
        
        while que:
            curr,C,d = que.popleft()
            
            
            for val,color in adjMap[curr]:
                
                if C == 'B' and color == 'R' and redAns[val] == float('inf'):
                    redAns[val] = d + 1
                    que.append([val,color,d + 1])
                elif C == 'R' and color == 'B' and blueAns[val] == float('inf'):
                    blueAns[val] = d + 1
                    que.append([val,color,d + 1])
        
        ans = []
        for a,b in zip(blueAns,redAns):
            x = min(a,b)
            x = x if x < float('inf') else -1
            ans.append(x)
        
        return ans