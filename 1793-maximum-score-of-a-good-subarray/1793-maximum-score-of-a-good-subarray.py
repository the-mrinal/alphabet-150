'''
1 4 3    7     4 5 
0 1 2    3     4 5

3



'''

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
    
        left = k
        right = k
        maxScore = nums[k]
        currScore = nums[k]
        n = len(nums)
        currMin = nums[k]

        while left >= 0 and right < n:
            leftNum,rightNum = 0,0

            if left > 0:
                leftNum = nums[left - 1]
            if right < n-1:
                rightNum = nums[right + 1]

            if leftNum >= rightNum and leftNum != 0:
                left -= 1
                currMin = min(currMin,nums[left])

            elif rightNum > leftNum:
                right += 1
                currMin = min(currMin,nums[right])

            currScore = currMin*(right - left + 1)
            maxScore = max(maxScore,currScore)
            if left == 0 and right == n - 1:
                break

        return maxScore
