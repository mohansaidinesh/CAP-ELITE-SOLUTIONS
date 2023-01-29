if root==None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        lc=self.lowestCommonAncestor(root.left,p,q)
        rc=self.lowestCommonAncestor(root.right,p,q)
        if lc!=None and rc!=None:
            return root
        if lc!=None:
            return lc
        if rc!=None:
            return rc
        if rc==None and lc==None:
            return None
