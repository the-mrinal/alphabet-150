# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        
        def helper(node: Optional[TreeNode]):
            nonlocal ans
            if not node:
                return None
            
            node.left = helper(node.left)
            node.right = helper(node.right)
            
            if node.val in to_delete:
                temp = []
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                ans = ans + temp
                return None
            
            return node
        head = helper(root)
        if head:
            ans = ans + [head]
        return ans
            