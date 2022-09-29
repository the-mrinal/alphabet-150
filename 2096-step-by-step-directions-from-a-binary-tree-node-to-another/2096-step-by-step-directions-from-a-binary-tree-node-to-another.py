# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findTarget(target):
            stack = [[root,'']]
            
            while stack:
                
                curr,path = stack.pop()
                
                if curr.val == target:
                    return path
                
                if curr.left:
                    stack.append([curr.left,path + 'L'])
                
                if curr.right:
                    stack.append([curr.right,path + 'R'])
            
            return ''
        
        startPath = findTarget(startValue)
        endPath = findTarget(destValue)
        
        res = []
        
        i = 0
        j = 0
        
        while i < len(startPath) and j < len(endPath) and startPath[i] == endPath[j]:
            i += 1
            j += 1
        
        res = len(startPath[i:])*'U' + endPath[j:]
        
        return res