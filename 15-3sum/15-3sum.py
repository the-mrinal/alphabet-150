class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []
        
        def findSum(first,left):
            nonlocal result
            right = n - 1
            while left < right:
                target = first + nums[left] + nums[right]
                
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    result.append([first,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left <= right and nums[left] == nums[left - 1]:
                        left += 1
        
        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            findSum(nums[i],i + 1)
        
        return result
            