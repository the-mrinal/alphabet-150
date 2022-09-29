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
                currTime = (dist * 2) + (((dist * 2) - 1)//pat)*pat
                timeReq = max(timeReq,currTime)
        
        return timeReq + 1