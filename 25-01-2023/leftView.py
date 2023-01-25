# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res={}
        def view(root,res,i):
            if root!=None:
                res[i]=root.val
                view(root.right,res,i+1)
                view(root.left,res,i+1)
                
        view(root,res,0)
        return res.values()
        
