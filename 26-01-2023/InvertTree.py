# Given the root of a binary tree, invert the tree, and return its root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = [root]
        while res:
            node = res.pop()
            if node:
                node.left, node.right = node.right, node.left
                res += node.left, node.right
        return root
