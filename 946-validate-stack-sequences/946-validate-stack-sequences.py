class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        n = len(pushed)
        stack = []
        while i < n and j < n:
            while  i < n and pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            if i < n and pushed[i] == popped[j]:
                stack.append(pushed[i])
                i += 1
            
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        
        return True if i == n and j == n else False