def attack(attacker, defender):
    defender.hp -= attacker.atk
    if defender.hp <= 0:
        return f"{defender.__class__.__name__} 를 쓰러뜨렸다!"
    return f"{defender.__class__.__name__} 에게 {attacker.atk} 데미지를 입힘 (남은 HP: {defender.hp})"
