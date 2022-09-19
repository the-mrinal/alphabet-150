class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        currSum = 0
        
        for i in range(1,len(prices)):
            currSum = max(0,currSum + prices[i] - prices[i - 1])
            maxSoFar = max(currSum,maxSoFar)
    
        return maxSoFar