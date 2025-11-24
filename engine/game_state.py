from engine.player import Player
from engine.map_data import MapData
from engine.entity import Monster
from engine.combat import attack

class GameState:
    def __init__(self):
        self.map_data = MapData()
        self.player = Player(5, 4)
        self.monsters = [Monster(12, 2, hp=20)]

    def player_move(self, dx, dy):
        new_x = self.player.x + dx
        new_y = self.player.y + dy
        if not self.map_data.is_block(new_x, new_y):
            self.player.move(dx, dy)

    def player_move_to(self, x, y):
        if not self.map_data.is_block(x, y):
            self.player.x = x
            self.player.y = y

    def player_attack(self):
        for m in self.monsters:
            if abs(m.x - self.player.x) <= 1 and abs(m.y - self.player.y) <= 1:
                return attack(self.player, m)
        return "주변에 공격할 몬스터가 없습니다."

    def render_map(self):
        grid = [list(row) for row in self.map_data.map]

        # Player
        grid[self.player.y][self.player.x] = "P"

        # Monsters
        for m in self.monsters:
            grid[m.y][m.x] = "M"

        return "\n".join("".join(row) for row in grid)
      
