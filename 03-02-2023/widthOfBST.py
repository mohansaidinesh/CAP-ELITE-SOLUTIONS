# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=collections.deque([[root,0]])
        print(q)
        print(q[0])
        res=0
        while q:
            res=max(res,(q[-1][1]-q[0][1])+1)
            for i in range(len(q)):
                [node,index]=q.popleft()
                if node.left:
                    q.append([node.left,2*index-1])
                if node.right:
                    q.append([node.right,2*index])
        return res
