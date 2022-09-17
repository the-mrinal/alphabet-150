class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
         
            prev = 0
            maxSoFar = 0
            
            for val in values:
                maxSoFar = max(maxSoFar,val + prev)
                
                prev = max(val,prev) - 1
            
            return maxSoFar