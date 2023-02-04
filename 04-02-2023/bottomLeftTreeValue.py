# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        q = deque([root])
        while q:
            root=q.popleft()
            if root.right:
                q.append(root.right)
            if root.left:
                q.append(root.left)
        return root.val
