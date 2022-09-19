class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def sanitise():
            stack = []
            ans = []
            n = len(s)
            to_remove = []
            for i in range(n):
                if s[i] == '(':
                    stack.append(i)
                elif s[i] == ')':
                    if stack:
                        stack.pop()
                    else:
                        to_remove.append(i)
                
            while stack:
                to_remove.append(stack.pop())
            
            for i in range(n):
                if i in to_remove:
                    continue
                ans.append(s[i])
        
            return ''.join(ans)
        return sanitise()
                    