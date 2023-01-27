# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr_count, max_count, prev_val, modes = 0, 0, None, []
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.curr_count = 1 if node.val != self.prev_val else self.curr_count + 1
            if self.curr_count > self.max_count: self.max_count, self.modes = self.curr_count, [node.val]
            elif self.curr_count == self.max_count: self.modes.append(node.val)
            self.prev_val = node.val
            dfs(node.right)
        dfs(root)
        return self.modes
        
