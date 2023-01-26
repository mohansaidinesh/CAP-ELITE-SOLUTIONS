# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind=inorder.index(postorder.pop(-1))
            root=TreeNode(inorder[ind])
            root.right=self.buildTree(inorder[ind+1:],postorder)
            root.left=self.buildTree(inorder[0:ind],postorder)
            return root
