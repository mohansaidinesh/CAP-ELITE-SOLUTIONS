# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p and q:
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            return p is q
        if not s: 
            return False
        if isSameTree(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
