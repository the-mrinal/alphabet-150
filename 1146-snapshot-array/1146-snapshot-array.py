class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = [defaultdict(int) for _ in range(length)]
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.snaps[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
    
        

    def get(self, index: int, snap_id: int) -> int:
        while snap_id not in self.snaps[index] and snap_id > 0:
            snap_id -= 1
        return self.snaps[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)