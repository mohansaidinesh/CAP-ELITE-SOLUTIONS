class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        k, v = rooms[0], {0}
        while k:
            r = k.pop(0)
            v.add(r)
            for i in rooms[r]:
                if i not in v:
                    k.append(i)
        return len(v)==len(rooms)
