# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root==None: 
            return 0
        def trav(root):
            return trav(root.left)+[root.val]+trav(root.right) if root else []
        l=trav(root)
        return min(l[i+1] - l[i] for i in range(len(l) - 1))
