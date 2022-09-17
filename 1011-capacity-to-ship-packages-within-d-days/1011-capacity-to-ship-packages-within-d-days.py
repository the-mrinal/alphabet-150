class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        def condition(currShipW):
            day = 1
            currW = 0
            for w in weights:
                currW += w
                
                if currW > currShipW:
                    day += 1
                    currW = w
                
                if day > days:
                    return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left