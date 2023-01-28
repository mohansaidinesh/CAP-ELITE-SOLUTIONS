# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], v: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(v)
        if v > root.val: 
            root.right = self.insertIntoBST(root.right, v)  
        else: 
            root.left = self.insertIntoBST(root.left, v) 
        return root
            
