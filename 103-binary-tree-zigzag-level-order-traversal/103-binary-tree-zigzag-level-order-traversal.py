# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        
        if root:
            que.append([root,0])
            
        res = []
        
        while que:
            curr,level = que.popleft()
            
            if level == len(res):
                res.append([])
            
            if level % 2 == 0:
                res[-1].append(curr.val)
            else:
                res[-1] = [curr.val] + res[-1]
            
            if curr.left:
                que.append([curr.left,level + 1])
            
            if curr.right:
                que.append([curr.right,level + 1])
            
        return res