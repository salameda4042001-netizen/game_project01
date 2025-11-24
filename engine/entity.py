class Entity:
    def __init__(self, x, y, hp=10, atk=3):
        self.x = x
        self.y = y
        self.hp = hp
        self.atk = atk

    def is_dead(self):
        return self.hp <= 0

    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, hp={self.hp}, atk={self.atk})"


class Monster(Entity):
    pass
