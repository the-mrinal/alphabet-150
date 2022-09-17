class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxVal = min(height[0],height[-1])*(n-1)
        start = 0
        end = n - 1
        while start < end:
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
            maxVal = max(maxVal,min(height[start],height[end])*(end - start))
        
        return maxVal