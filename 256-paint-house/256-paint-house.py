class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        dp = [[0 for _ in range(3)] for _ in range(n)]
        
        dp[0] = costs[0]
        
        for i in range(1,n):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][:j]+dp[i - 1][j+1:]) + costs[i][j]

        return min(dp[n-1])