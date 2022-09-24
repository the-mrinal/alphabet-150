class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        
        
        dp = [[0 for _ in range(k)]for _ in range(n)]
        
        dp[0] = costs[0]
        
        for i in range(1,n):
            for j in range(k):
                dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
        
        return min(dp[n-1])