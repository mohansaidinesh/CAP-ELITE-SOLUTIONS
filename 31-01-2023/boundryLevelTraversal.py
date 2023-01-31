#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        res=[]
        def lefts(root):
            if root:
                if root.left:
                    res.append(root.data)
                    lefts(root.left)
                elif root.right:
                    res.append(root.data)
                    lefts(root.right)
        def rights(root):
            if root:
                if root.right:
                    rights(root.right)
                    res.append(root.data)
                elif root.left:
                    rights(root.left)
                    res.append(root.data)
        def leaf(root):
            if root:
                leaf(root.left)
                if root.left==None and root.right==None:
                    res.append(root.data)
                leaf(root.right)
        if root:
            res.append(root.data)
            lefts(root.left)
            leaf(root.left)
            leaf(root.right)
            rights(root.right)
        return res
