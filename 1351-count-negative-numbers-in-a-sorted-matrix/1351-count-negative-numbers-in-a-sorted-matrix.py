class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        totalCount = 0
        m = len(grid)
        n = len(grid[0])
        
        def binarySearch(nums):
            nonlocal n
            
            left = 0
            right = n - 1
            
            def condition(mid):
                if nums[mid] >= 0:
                    return False
                return True
            
            while left < right:
                mid = left + (right - left) // 2
                
                if condition(mid):
                    right = mid
                else:
                    left = mid + 1
            
            return n - left if nums[left] < 0 else 0
        
        for nums in grid:
            totalCount +=  binarySearch(nums)
        
        return totalCount