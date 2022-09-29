class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        currSum = 0
        maxSize = float('inf')
        maxSum = 0
        for end in range(len(nums)):
            currSum += nums[end]
            
            if currSum >= target:
                while currSum > target and start <= end:
                    currSum -= nums[start]
                    start += 1
                
                if currSum < target:
                    start -= 1
                    currSum += nums[start]
                
                if maxSize > (end - start + 1):
                    maxSum = currSum
                    maxSize = end - start + 1
            
        
        return maxSize if maxSize < float('inf') else 0