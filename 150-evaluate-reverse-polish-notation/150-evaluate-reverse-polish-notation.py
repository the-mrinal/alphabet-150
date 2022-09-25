class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['/','+','-','*']
        n = len(tokens)
        
        def solve(A,B,symbol):
            if symbol == '+':
                return A + B
            if symbol == '-':
                return B - A
            if symbol == '*':
                return A * B
            if symbol == '/':
                isNeg = 1
                if (A < 0 or B < 0) and not (A < 0 and B < 0):
                    isNeg = -1
                
                return isNeg * (abs(B) // abs(A))
            

        
        
        for i in range(n):
            if tokens[i] in op:
                one = stack.pop()
                two = stack.pop()
                ans = str(solve(int(one),int(two),tokens[i]))
                stack.append(ans)
            else:
                stack.append(tokens[i])
        
        return stack[0]