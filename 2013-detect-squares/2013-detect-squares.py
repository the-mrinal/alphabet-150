class DetectSquares:

    def __init__(self):
        self.countPoints = Counter()
        

    def add(self, point: List[int]) -> None:
        self.countPoints[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x,y = point
        for pointB,count in self.countPoints.items():
            x2,y2 = pointB
            if abs(x - x2) == 0 or abs(x - x2) != abs(y - y2):
                continue
            ans += count * self.countPoints[(x,y2)] * self.countPoints[(x2,y)]
        
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)