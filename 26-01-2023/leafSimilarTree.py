# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1=[]
        r2=[]
        
        def leaf(root,r):
            if root==None:
                return 
            if root.left==None and root.right==None:
                r.append(root.val)
            leaf(root.left,r)
            leaf(root.right,r)
        leaf(root1,r1)
        leaf(root2,r2)
        return r1==r2

        
        
