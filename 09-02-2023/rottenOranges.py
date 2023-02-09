class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        r=len(mat)
        c=len(mat[0])
        fc=0
        rt=[]
        for i in range(r):
            for j in range(c):
                if mat[i][j]==2:
                    rt.append((i,j))
                elif mat[i][j]==1:
                    fc+=1
        mins=0
        l=[(0,-1),(-1,0),(0,1),(1,0)]
        while rt and fc >0:
            mins+=1
            for _ in range(len(rt)):
                x,y =rt.pop(0)
                for m,n in l:
                    nx,ny=x+m,y+n
                    if nx < 0 or nx == r or ny < 0 or ny == c:
                                continue
                    if mat[nx][ny]==0 or mat[nx][ny]==2:
                        continue
                    fc-=1
                    mat[nx][ny]=2
                    rt.append((nx,ny))
        return mins if fc==0 else -1
