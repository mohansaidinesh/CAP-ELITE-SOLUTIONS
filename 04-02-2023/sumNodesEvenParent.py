# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum=0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root==None:
            return 0
        if root.val%2==0:
            if root.left and root.left.left:
                self.sum+=root.left.left.val
            if root.left and root.left.right:
                self.sum+=root.left.right.val
            if root.right and root.right.left:
                self.sum+=root.right.left.val
            if root.right and root.right.right:
                self.sum+=root.right.right.val
        self.sumEvenGrandparent(root.left)
        self.sumEvenGrandparent(root.right)
        return self.sum
