class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = [[sum(row),index] for index,row in enumerate(mat)]
        
        ans = []
        count = 0
        for val,index in power:
            count += 1
            if count <= k:
                heappush(ans,[-val,-index])
            else:
                if -ans[0][0] > val:
                    heappop(ans)
                    heappush(ans,[-val,-index])
        result = []
        while ans:
            result.append(-heappop(ans)[1])
        
        return result[::-1]
        