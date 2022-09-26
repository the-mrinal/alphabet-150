class Solution:
    def fourSum(self, num: List[int], K: int) -> List[List[int]]:
        def twoSum(nums,target):
            left = 0
            right = len(nums) - 1
            ans = []
            
            while left < right:
                number = nums[left] + nums[right]
                if number < target:
                    left += 1
                elif number > target:
                    right -= 1
                else:
                    ans.append([nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left <= right:
                        left += 1
            return ans
        
        def kSum(nums,target,k):
            if not nums:
                return []
            if k == 2:
                return twoSum(nums,target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for subsets in kSum(nums[i+1:],target - nums[i],k - 1):
                        res.append([nums[i]] + subsets)

            return res

        num.sort()
        
        return kSum(num,K,4)