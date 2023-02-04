# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    c=0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def trav(root):
            if root:
                self.c+=1
                return self.countNodes(root.left) and self.countNodes(root.right)
        trav(root)
        return self.c
