# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] 
        ans=[]
        def traverse(node, i):
            if node!=None:
                if i < len(res):
                    res[i].append(node.val)     
                else:
                    res.append([node.val])    
                traverse(node.left, i+1)      
                traverse(node.right, i+1)       
        traverse(root, 0)                        
        if len(res)==0 or len(res)==1:
            return res
        else:
            for i in range(0,len(res)):
                if i%2==0:
                    ans.append(res[i])
                else:
                    ans.append(res[i][::-1])
        return ans
