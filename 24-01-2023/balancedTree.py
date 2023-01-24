# Given a binary tree, determine if it is height-balanced
# Input: root = [3,9,20,null,null,15,7]
# Output: true
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None: 
            return 1
        lc = self.isBalanced(root.left)
        rc=self.isBalanced(root.right)
        if lc == 0 or rc==0: 
            return 0
        if abs(lc - rc) > 1: 
            return 0
        return max(lc, rc) + 1
