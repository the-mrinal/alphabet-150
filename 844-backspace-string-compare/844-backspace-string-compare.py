class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def findFinalWord(S):
            stack = []
            for w in S:
                if w == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(w)
            return "".join(stack)
        
        return findFinalWord(s) == findFinalWord(t)