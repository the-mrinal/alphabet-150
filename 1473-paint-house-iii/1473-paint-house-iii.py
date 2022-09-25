class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        cache = {}
        
        def paintHouse(index,neigh,color):
            nonlocal cache
            if index == m or neigh < 0 or (m - index) < neigh:
                return 0 if index == m and neigh == 0 else float('inf')
            

            key = (index,neigh,color)
            
            if key not in cache:
                if houses[index] == 0:
                    cache[key] = min(paintHouse(index + 1,neigh - (color != curr_color),curr_color)+cost[index][curr_color -1] for curr_color in range(1,n+1))
                else:
                    cache[key] = paintHouse(index + 1,neigh - (color != houses[index]),houses[index])
            
            return cache[key]
        
        paintHouse(0,target,-1)
        key = (0,target,-1)
        return cache[key] if cache[key] < float('inf') else -1