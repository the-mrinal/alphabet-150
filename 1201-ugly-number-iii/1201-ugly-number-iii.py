class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = min(a,b,c)
        right = 10**10
        
        def findLCM(a,b):
            return (a*b) // math.gcd(a,b)
        
        ab = findLCM(a,b)
        bc = findLCM(b,c)
        ac = findLCM(a,c)
        abc = findLCM(ab,c)
        
        
        def condition(num):
            count = num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc
            return count >= n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    