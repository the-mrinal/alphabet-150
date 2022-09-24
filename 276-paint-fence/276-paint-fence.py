class Solution:
    def numWays(self, n: int, k: int) -> int:

        if n == 1:
            return k
        if n == 2:
            return k*k 

        
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = k
        dp[2] = k * k
        
        for i in range(3,n+1):
            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
        
        return dp[n]