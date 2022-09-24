class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxVDiff = 0
        maxHDiff = 0
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        hCuts = [0] + horizontalCuts + [h]
        vCuts = [0] + verticalCuts + [w]
        
        for i in range(1,len(hCuts)):
            maxHDiff  = max(maxHDiff,hCuts[i] - hCuts[i - 1])
        
        for j in range(1,len(vCuts)):
            maxVDiff = max(maxVDiff,vCuts[j] - vCuts[j - 1])
        
        return (maxHDiff * maxVDiff)%(10**9 + 7)