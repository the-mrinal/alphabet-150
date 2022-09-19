class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        leftSweep = [1]*n
        rightSweep = [1]*n
        
        
        prev = ratings[0]
        for i in range(1,n):
            if ratings[i] > prev:
                leftSweep[i] = leftSweep[i - 1] + 1
            prev = ratings[i]
        
        
        prev = ratings[-1]
        for i in range(n-2,-1,-1):
            if ratings[i] > prev:
                rightSweep[i] = rightSweep[i + 1] + 1
            prev = ratings[i]
        
        totalMinSum = 0
        
        for l,r in zip(leftSweep,rightSweep):
            totalMinSum += max(l,r)
        
        return totalMinSum