# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        lc=self.lowestCommonAncestor(root.left,p,q)
        rc=self.lowestCommonAncestor(root.right,p,q)
        if lc!=None and rc!=None:
            return root
        if lc!=None:
            return lc
        if rc!=None:
            return rc
        if rc==None and lc==None:
            return None
