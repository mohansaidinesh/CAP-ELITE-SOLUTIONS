"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    d={}
    q=[]
    q.append((root,0))
    while(q):
        i=q.pop(0)
        if i[1] not in d:
            d[i[1]]=i[0].info
        if i[0].left:
            q.append((i[0].left,i[1]-1))
        if i[0].right:
            q.append((i[0].right,i[1]+1))  
    for i,j in sorted(d.items()):
        print(str(j),end=" ")
