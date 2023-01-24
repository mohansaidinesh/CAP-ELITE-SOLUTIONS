# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root!=None else []
