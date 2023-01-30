def mirror(node):
    if (node == None):
        return
    else:
        temp = node
        mirror(node.left)
        mirror(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp
