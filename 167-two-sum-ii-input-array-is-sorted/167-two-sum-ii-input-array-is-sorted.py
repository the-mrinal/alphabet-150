'''

traverse 0 - n
    - otherHalf = target - (nums[i])

'''




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def searchTarget(val,index):
            left = index
            right = n - 1
            
            while left <= right:
                mid = left + (right - left)//2
                
                if nums[mid] < val:
                    left = mid + 1
                elif nums[mid] > val:
                    right = mid - 1
                else:
                    return mid
            return n        
        
            
        ans = []
        for i in range(n):
            otherVal = searchTarget(target - nums[i],i+1)
            
            if (otherVal < n and nums[otherVal] + nums[i] == target):
                return [i + 1,otherVal + 1]
        
        return []
            
            
            
            
        
        
        