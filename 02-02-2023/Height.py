# The height of a binary tree is the number of edges between the tree's root and its furthest leaf. 
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(r):
    l=0
    rc=0
    if r.left:
        l=height(r.left)+1
    if r.right:
        rc=height(r.right)+1
    return max(l,rc)
