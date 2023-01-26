# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        def trav(root,i):
            if root==None:
                return []
            if i<len(res):
                res[i].append(root.val)
            else:
                res.append([root.val])
            trav(root.left,i+1)
            trav(root.right,i+1)
        trav(root,0)
        k=[]
        for i in res:
            k.append(sum(i)/len(i))
        return k
