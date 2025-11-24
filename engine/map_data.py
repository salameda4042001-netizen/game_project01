import os

class MapData:
    def __init__(self):
        path = os.path.join("assets", "map.txt")
        with open(path, "r", encoding="utf-8") as f:
            self.map = [list(line.rstrip("\n")) for line in f]

    def is_block(self, x, y):
        if y < 0 or y >= len(self.map):
            return True
        if x < 0 or x >= len(self.map[0]):
            return True
        return self.map[y][x] == "#"
