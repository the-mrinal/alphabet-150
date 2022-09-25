class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        
        n = len(bloomDay)
        
        if m*k > n:
            return -1
        
        def condition(mid):
            nonlocal n
            bouq = 0
            flow = 0
            
            for i in range(n):
                if bloomDay[i] > mid:
                    flow = 0
                else:
                    flow += 1
                    bouq += flow // k
                    flow = flow % k
            
            return bouq >= m
        
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left