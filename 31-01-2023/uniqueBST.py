class Solution:
    def numTrees(self, n: int) -> int:
        l=[0]*(n+1) 
        l[0]=1
        l[1]=1
        for i in range(2,n+1) :
            for j in range(1,i+1) :
                l[i]=l[i]+(l[i-j]*l[j-1]) 
        return l[n]
        
