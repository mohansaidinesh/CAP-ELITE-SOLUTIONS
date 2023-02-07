class Solution:
    def findCenter(self, l: List[List[int]]) -> int:
        if l[0][0]==l[1][0] or l[0][0]==l[1][1]:
            return l[0][0]
        return l[0][1]
