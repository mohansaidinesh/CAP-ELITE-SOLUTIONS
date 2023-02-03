# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    c = 0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def trav(r):
            if r==None:
                return 0
            lc=trav(r.left)
            rc=trav(r.right)
            self.c += abs(lc - rc)
            return r.val+lc+rc
        trav(root)
        return self.c
        
