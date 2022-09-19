class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a,b,c = 0,0,0
        
        for num in nums:
            options = [a + num,b+num,c +num]
            for opt in options:
                if opt%3 == 0:
                    a = max(opt,a)
                elif opt%3 == 1:
                    b = max(opt,b)
                else:
                    c = max(opt,c)
            
        return a