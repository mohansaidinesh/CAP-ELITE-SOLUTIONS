# A binary tree is uni-valued if every node in the tree has the same value.
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        n=root.val
        def trav(root):
            if root==None:
                return True
            if root.val!=n: 
                return False
            else:
                return  trav(root.left) and trav(root.right)
        return trav(root)
        
        
