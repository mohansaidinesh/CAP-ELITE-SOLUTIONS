"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    s=list(s)
    s=[int(i) for i in s]
    while len(s)!=0 :
        trav(root,s)
def trav(root,s):
    if root.left==None and root.right==None:
        print(root.data,end="")
        return
    if len(s)==0:
        return
    x=s[0]
    del s[0]
    if x==0:
        trav(root.left,s)
    else:
        trav(root.right,s)
        
