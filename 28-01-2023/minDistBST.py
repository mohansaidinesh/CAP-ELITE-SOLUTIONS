# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def trav(r):
            if r==None:
                return []
            return trav(r.left)+[r.val]+trav(r.right)
        l=trav(root)
        k=[]
        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                k.append(l[j]-l[i])
        return min(k)
        
