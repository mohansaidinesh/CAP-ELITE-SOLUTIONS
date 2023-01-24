# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []                                
        def traverse(node, i):
            if node!=None:
                if i < len(res):
                    res[i].append(node.val)     
                else:
                    res.append([node.val])    
                traverse(node.left, i+1)      
                traverse(node.right, i+1)       
        traverse(root, 0)                        
        return res
