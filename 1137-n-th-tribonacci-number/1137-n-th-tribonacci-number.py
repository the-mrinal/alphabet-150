class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        t3 = t0 + t1 + t2
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        
        for i in range(3,n):
            t0 = t1
            t1 = t2
            t2 = t3
            t3 = (t0 + t1 + t2)
            
        
        return t3