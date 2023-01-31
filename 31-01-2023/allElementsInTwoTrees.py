# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, r: TreeNode, s: TreeNode) -> List[int]:
        def trav(root) :
            return trav(root.left) +[root.val]+trav(root.right) if root else []
        l=trav(r) 
        k=trav(s) 
        return sorted(l+k) 
        
