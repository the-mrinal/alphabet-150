class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        
        adjMap = defaultdict(list)
        
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        
        short = [0]*n
        
        que = deque()
        
        que.append([0,0])
        visited = set()
        visited.add(0)
        
        while que:
            curr,dist = que.popleft()
            
            short[curr] = dist
            
            for child in adjMap[curr]:
                if child not in visited:
                    que.append([child,dist + 1])
                    visited.add(child)
        
        timeReq = 0
        for dist,pat in zip(short,patience):
            if pat > 0:
                offset = (dist*2) % pat if (dist*2) % pat > 0 else pat 
                currTime = (dist * 2)*2 - offset
                timeReq = max(timeReq,currTime)
        
        return timeReq + 1