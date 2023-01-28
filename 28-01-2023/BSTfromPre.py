# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, p: List[int]) -> Optional[TreeNode]:
        if len(p)==0:
            return None
        root=TreeNode(p[0])
        root.left=self.bstFromPreorder([i for i in p if i<root.val])
        root.right=self.bstFromPreorder([i for i in p if i>root.val])
        return root
