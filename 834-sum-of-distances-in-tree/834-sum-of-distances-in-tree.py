class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        count = [1]*n
        ans = [0]*n
        
        def findTotalSum():
            que = deque()
            que.append([0,0])
            
            visited = set()
            visited.add(0)
            
            totalSum = 0
            
            while que:
                curr,depth = que.popleft()
                
                totalSum += depth
                
                for child in adjMap[curr]:
                    if child not in visited:
                        que.append([child,depth + 1])
                        visited.add(child)
            
            return totalSum
        
        def countNodes(root=0,parent=None):
            for child in adjMap[root]:
                if child != parent:
                    countNodes(child,root)
                    count[root] += count[child]
            
            
        
        totalSum = findTotalSum()
        
        countNodes()
        
        
        
        ans[0] = totalSum
        
        que = deque()
        que.append([0,None])
        visited = set()
        visited.add(0)
        while que:
            curr,par = que.popleft()
            
            for child in adjMap[curr]:
                if child not in visited:
                    ans[child] = ans[curr] - count[child] + (n - count[child])

                    que.append([child,curr])
                    visited.add(child)
                
        return ans
        