# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return 0
        if root.val==targetSum and root.left== None and root.right== None:
            return 1
        return self.hasPathSum(root.left,targetSum-root.val)  or self.hasPathSum(root.right,targetSum-root.val) 
