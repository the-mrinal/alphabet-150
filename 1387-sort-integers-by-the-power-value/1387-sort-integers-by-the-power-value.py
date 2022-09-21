class Solution:
    
    def __init__(self):
        self.cache = {1:0}
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def findPower(val):
            if val not in self.cache:
                nextVal = val // 2 if val % 2 == 0 else (3*val + 1)
                
                power = findPower(nextVal)
                
                self.cache[val] = 1 + power
            return self.cache[val]
        
        maxHeap = []
        count = 0
        for i in range(lo,hi + 1):
            count += 1
            value = findPower(i)
            if count <= k:
                heappush(maxHeap,[-value,-i])
            elif -maxHeap[0][0] > value:
                heappop(maxHeap)
                heappush(maxHeap,[-value,-i])
        # print(maxHeap)
        return -maxHeap[0][1]