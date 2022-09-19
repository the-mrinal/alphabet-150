class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = set(nums)
        maxVal = 0
        for num in nums:
            if num - 1 in freq:
                continue
            count = 0
            temp = num
            while temp in freq:
                count += 1
                temp += 1
            maxVal = max(maxVal,count)
        
        return maxVal