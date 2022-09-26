class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalSum = sum(chalk)
        
        target = k % totalSum
        
        for index,c in enumerate(chalk):
            if c > target:
                return index
            target -= c
        
        return 0