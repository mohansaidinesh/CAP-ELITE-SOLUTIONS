# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def trav(root):
            return trav(root.left)+[root.val]+trav(root.right) if root else []
        def inh(l):
            if not l:
                return 
            m=len(l)//2
            return TreeNode(l[m],inh(l[:m]),inh(l[m+1:]))    
        l=trav(root)
        return inh(l)
