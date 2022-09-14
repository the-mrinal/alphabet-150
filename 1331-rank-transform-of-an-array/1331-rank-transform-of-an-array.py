class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        temp = []
        for index,val in enumerate(arr):
            temp.append([val,index])
        
        temp.sort()
        
        res = [1]*n
        
        count = 1
        prev = None
        
        for x,y in temp:
            if prev is not None:
                count = count + 1 if prev < x else count
            res[y] = count
            prev = x
        
        return res