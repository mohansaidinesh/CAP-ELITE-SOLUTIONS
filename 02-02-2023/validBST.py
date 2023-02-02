""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def trav(root):
        return trav(root.left)+[root.data]+trav(root.right) if root else []
    k=trav(root)
    return k==sorted(k) and len(set(k))==len(k)
