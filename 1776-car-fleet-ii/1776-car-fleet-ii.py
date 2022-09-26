'''
n cars
same direction

1 2 | 2 1

1 + x*2 == 2 + x*1
2x - x = 2 - 1
x = 1

[3,1] [p_a,s_a] [p_b,s_b]

p_a + s_sx = p_b + s_bx

(s_s - s_b)x = (p_b - p_a)

x = (p_b-p_a)/(s_s - s_b)



'''

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        
        stack = []
        res = [-1]*n
        
        for i in range(n-1,-1,-1):
            p,s = cars[i]
            while stack and (s <= cars[stack[-1]][1] or (cars[stack[-1]][0] - p)/(s - cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)
        
        return res
    
    
            # while stack and (s <= cars[stack[-1]][1] or (cars[stack[-1]][0])/(s - cars[stack[-1]][1]) >= res[stack[-1]] > 0):
# 
#             while stack and (s <= A[stack[-1]][1] or (A[stack[-1]][0] - p) / (s - A[stack[-1]][1]) >= res[stack[-1]] > 0):
    
    
    