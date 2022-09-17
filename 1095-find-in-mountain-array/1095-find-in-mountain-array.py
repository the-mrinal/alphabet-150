# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        
        
        
        def findPeak():
            left = 1
            right = size - 2
            
            def condition(peakIndex):
                peakV = mountain_arr.get(peakIndex)
                prevV = mountain_arr.get(peakIndex - 1)
                
                if prevV < peakV:
                    return False
                return True
            
            while left < right:
                mid = left + (right - left) // 2
                
                if condition(mid):
                    right = mid
                else:
                    left = mid + 1
                
            return left - 1
        
        def findTargetAsc(start,end):
            left = start
            right = end
            
            def condition(mid):
                currV = mountain_arr.get(mid)
                if currV >= target:
                    return True
                return False
            while left < right:
                mid = left + (right - left) // 2
                
                if condition(mid):
                    right = mid
                else:
                    left = mid + 1
                
            return left
        
        def findTargetDsc(start,end):
            left = start
            right = end
            
            def condition(mid):
                currVal = mountain_arr.get(mid)
                if currVal >= target:
                    return True
                return False
            
            while left < right:
                mid = left + (right - left + 1)//2 
                
                if condition(mid):
                    left = mid
                else:
                    right = mid - 1
            
            return left
        
        peakIndex = findPeak()
        
        ans = findTargetAsc(0,peakIndex)
        if ans < size and mountain_arr.get(ans) == target:
            return ans
        ans = findTargetDsc(peakIndex+1,size - 1)
        
        if ans < size and ans >= 0 and  mountain_arr.get(ans) == target:
            return ans
        
        return -1
        
            