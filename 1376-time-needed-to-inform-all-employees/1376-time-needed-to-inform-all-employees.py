class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_map = defaultdict(list)
        
        for index,val in enumerate(manager):
            if index == headID:
                continue
            manager_map[val].append(index)
        
        
        def findMaxInformTime(eID):
            if eID not in manager_map:
                return informTime[eID]
            currTime = informTime[eID]
            
            maxTime = 0
            for child in manager_map[eID]:
                maxTime = max(maxTime,findMaxInformTime(child))
            return currTime + maxTime
        
        return findMaxInformTime(headID)