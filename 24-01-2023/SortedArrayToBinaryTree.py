# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, n: List[int]) -> Optional[TreeNode]:
        if not n: return None                                 
        m = len(n)//2
        return TreeNode(n[m],self.sortedArrayToBST(n[:m]),self.sortedArrayToBST(n[m+1:]))    
