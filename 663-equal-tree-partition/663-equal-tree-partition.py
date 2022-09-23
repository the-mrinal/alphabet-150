# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        seen = []
        
        def findSum(node):
            if not node:
                return 0
            seen.append(node.val + findSum(node.left) + findSum(node.right))
            
            return seen[-1]
        
        total = findSum(root)
        seen.pop()
        return total / 2 in seen
    