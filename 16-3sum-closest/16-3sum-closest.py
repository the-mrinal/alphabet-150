class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        def findSum(first):
            left = first + 1
            right = n - 1
            localSum = float('inf')
            
            while left < right:
                num = nums[left] + nums[right] + nums[first]
                if abs(localSum - target) > abs(num - target):
                    localSum = num
                
                if num - target < 0:
                    left += 1
                elif num - target > 0:
                    right -= 1
                else:
                    return num           
            
            return localSum
        
        minSum = float('inf')
        for i in range(n):
            currSum = findSum(i)
            if currSum == target:
                return currSum
            else:
                if abs(minSum - target) > abs(currSum - target):
                    minSum = currSum
        
        return minSum