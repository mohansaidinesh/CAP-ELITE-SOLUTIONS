# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def trav(root) :
            if root==None:
                return []
            return trav(root.left)+[root.val]+trav(root.right) 
        l=trav(root)
        print(l) 
        lo=l.index(low) 
        h=l.index(high) 
        l1=l[lo:h+1]
        return sum(l1) 
            
        
        
