class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        maxSoFar = float('-inf')
        
        for i in range(len(nums)):
            t = max(nums[i],nums[i]*currMax,nums[i]*currMin)
            currMin = min(nums[i],currMax*nums[i],currMin*nums[i])
            currMax = t
            maxSoFar = max(maxSoFar,currMax)
        
        return maxSoFar