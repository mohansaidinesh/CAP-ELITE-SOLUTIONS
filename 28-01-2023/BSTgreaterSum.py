# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.v=0
        def trav(root,):
            if root==None:
                return 
            trav(root.right)
            self.v+=root.val
            root.val=self.v
            trav(root.left)
        trav(root)
        return root
