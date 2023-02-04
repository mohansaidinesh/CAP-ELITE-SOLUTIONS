# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        l = []
        def trav(root,i):
            if i == len(l): 
                l.append(root.val)
            else: 
                l[i] += root.val
            if root.left: 
                trav(root.left, i+1)
            if root.right: 
                trav(root.right, i+1)
        trav(root, 0)
        return l[-1]      
