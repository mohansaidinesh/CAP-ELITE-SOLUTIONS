# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymtrc(n1 = root, n2 = root):
            if not (n1 or n2):
                return True
            elif not (n1 and n2):
                return False
            elif n1.val != n2.val:
                return False
            return isSymtrc(n1.left, n2.right) and isSymtrc(n1.right, n2.left)
        return isSymtrc()
