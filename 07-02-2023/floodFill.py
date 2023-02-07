class Solution:
    def floodFill(self, img: List[List[int]], s: int, d: int, c: int) -> List[List[int]]:
        r=len(img)
        col=len(img[0])
        clr=img[s][d]
        if clr==c:
            return img
        def trav(s,d):
            img[s][d]=c
            if s-1>=0 and img[s-1][d] ==clr:
                trav(s-1,d)
            if d-1>=0 and img[s][d-1] ==clr:
                trav(s,d-1)
            if s+1<r and img[s+1][d] ==clr:
                trav(s+1,d)
            if d+1<col and img[s][d+1] ==clr:
                trav(s, d+1)
        trav(s,d)
        return img
