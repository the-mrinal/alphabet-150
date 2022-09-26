class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        totalSum = sum(nums)
        n = len(nums)
        target = totalSum - x
        
        minOp = float('-inf')
        
        start = 0
        currSum = 0
        
        for end in range(n):
            currSum += nums[end]
            
            while currSum > target and start <= end:
                currSum -= nums[start]
                start += 1
            
            if currSum == target:
                minOp = max(minOp,(end - start + 1))

        
        return n- minOp if minOp > float('-inf') else -1