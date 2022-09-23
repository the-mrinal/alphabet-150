# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def findCoins(node):
            if not node:
                return 0
            # if node.val == 0 and availCoins == 0:
            #     return -1
            
            subLeft = findCoins(node.left)
            
            subRight = findCoins(node.right)
            self.ans += abs(subLeft) + abs(subRight)   
            return node.val - 1 + subRight + subLeft
        
        findCoins(root)
        return self.ans