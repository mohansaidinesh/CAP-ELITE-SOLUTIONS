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
