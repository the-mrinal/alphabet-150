class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            temp = [0]*(i + 1)
            temp[0] = 1
            temp[-1] = 1
            for i in range(1,i):
                temp[i] = ans[-1][i - 1] + ans[-1][i]
            ans.append(temp)
        return ans
                