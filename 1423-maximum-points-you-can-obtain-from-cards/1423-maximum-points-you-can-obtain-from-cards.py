class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = k - 1
        j = len(cardPoints)
        
        index = 0
        currSum = sum(cardPoints[:i+1])
        maxSoFar = currSum
        
        while index < k:
            currSum -= cardPoints[i]
            
            i -= 1
            j -= 1
            index += 1
            
            currSum += cardPoints[j]
            
            maxSoFar = max(maxSoFar,currSum)
            
        
        return maxSoFar