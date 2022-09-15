class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        start = 0
        currSum = 0
        n = len(arr)
    
        smallest_len_sum_index = [float('inf')]*n
        curr_smallest_len_sum = float('inf')
        best_smallest_sum = float('inf')
        count = 0
    
        for end in range(n):
            currSum += arr[end]
            
            while currSum > target and start <= end:
                currSum -= arr[start]
                start += 1
            
            if currSum == target:
                currLength = end - start + 1
                if start > 0 and smallest_len_sum_index[start - 1] != float('inf'):
                    best_smallest_sum = min(smallest_len_sum_index[start - 1] + currLength,best_smallest_sum)
                curr_smallest_len_sum = min(curr_smallest_len_sum,currLength)
            smallest_len_sum_index[end] = curr_smallest_len_sum
                                
    

        return -1 if best_smallest_sum == float('inf') else best_smallest_sum