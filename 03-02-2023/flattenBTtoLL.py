# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    p=None
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root==None:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.p
        root.left = None
        self.p = root
        
        
