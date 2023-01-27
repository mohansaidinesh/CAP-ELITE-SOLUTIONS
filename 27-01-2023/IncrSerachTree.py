# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def trav(node):
            if node==None:    
                return []
            return trav(node.left) + [node.val] + trav(node.right)
        l = trav(root)
        ans = temp = TreeNode(l[0])
        for i in range(1, len(l)):
            temp.right = TreeNode(l[i])
            temp = temp.right
        return ans
