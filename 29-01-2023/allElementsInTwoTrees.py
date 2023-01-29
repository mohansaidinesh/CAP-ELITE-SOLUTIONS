# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def trav(root):
            return trav(root.left)+[root.val]+trav(root.right) if root else []
        l1=trav(root1)
        l2=trav(root2)
        return sorted(l1+l2)
        
