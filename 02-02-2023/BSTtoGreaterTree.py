# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    c=0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return
        self.convertBST(root.right)
        root.val+=self.c
        self.c=root.val
        self.convertBST(root.left)
        return root
