class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        currMax = 0
        maxSoFar = 0
        n = len(nums)
        visited = {}
        
        for end in range(n):
            if nums[end] not in visited:
                currMax += nums[end]
            else:
                maxSoFar = max(maxSoFar,currMax)
        
                temp = start
                start = visited[nums[end]] + 1

                while temp < start:
                    currMax -= nums[temp]
                    del visited[nums[temp]]
                    temp += 1
                currMax += nums[end]
            visited[nums[end]] = end
        maxSoFar = max(maxSoFar,currMax)
    
        
        return maxSoFar