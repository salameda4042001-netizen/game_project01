class Player:
    def __init__(self, x, y, hp=30, atk=5):
        self.x = x
        self.y = y
        self.hp = hp
        self.atk = atk

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"Player(x={self.x}, y={self.y}, hp={self.hp}, atk={self.atk})"
