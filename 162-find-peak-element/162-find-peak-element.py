'''
mid 



'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right =  len(nums) - 1
        
        
        
        def condition(mid):
            if nums[mid]<= nums[mid + 1]:
                return False
            
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    