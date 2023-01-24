#Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        lc=self.minDepth(root.left)
        rc=self.minDepth(root.right)
        if lc==0:
            return rc+1
        if rc==0:
            return lc+1
        return min(lc,rc)+1
