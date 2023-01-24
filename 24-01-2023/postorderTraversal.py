# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return  self.postorderTraversal(root.left) +  self.postorderTraversal(root.right)+[root.val]  if root!=None else []
