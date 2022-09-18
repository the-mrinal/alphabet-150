# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        que = deque()
        if root:
            que.append([root,[root.val]])
        res = []
        while que:
            curr,path = que.popleft()
            
            if not curr.left and not curr.right:
                if sum(path) == targetSum:
                    res.append(path.copy())
            
            if curr.left:
                que.append([curr.left,path + [curr.left.val]])
            
            if curr.right:
                que.append([curr.right,path + [curr.right.val]])
        
        return res