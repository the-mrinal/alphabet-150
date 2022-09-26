class Solution:
    def minPartitions(self, n: str) -> int:
        maxVal = -1
        for c in n:
            maxVal = max(maxVal,int(c))
        
        return maxVal