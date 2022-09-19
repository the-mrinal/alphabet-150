class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev = triangle[-1]
        curr = [0]*(n-1)
        
        for i in range(n-2,-1,-1):
            for j in range(i + 1):
                curr[j] = triangle[i][j] + min(prev[j],prev[j + 1])
            curr,prev = [0]*(i),curr
        
        return prev[0]