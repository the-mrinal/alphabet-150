# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i in range(len(inorder)):
            index_map[inorder[i]] = i
        
        preorderIndex = 0
        
        def BTreeConst(st,end):
            nonlocal preorderIndex,index_map
            if st > end:
                return None
            
            curr_root_val = preorder[preorderIndex]
            
            curr_root_index = index_map[curr_root_val]
            
            curr_node = TreeNode(curr_root_val)
            preorderIndex += 1
            
            curr_node.left = BTreeConst(st,curr_root_index -1)
            
            curr_node.right = BTreeConst(curr_root_index + 1,end)
            
            return curr_node
        
        return BTreeConst(0,len(inorder) - 1)
    