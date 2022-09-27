class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [float(target - p)/s for p,s in sorted(zip(position,speed))]
        
        res ,cur = 0,0
        
        for time in cars[::-1]:
            if time > cur:
                res += 1
                cur = time
        
        return res