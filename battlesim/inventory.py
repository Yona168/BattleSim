class Inventory:
    def __init__(self, armor, weapons, other_items):
        self.armor=armor
        self.weapons=weapons
        self.other_items=other_items

    def all_items():
        for piece in armor:
            yield piece
        for weapon in weapons:
            yield weapon
        for other_item in other_items:
            yield other_item

    def current_weapon(self):
        return self.weapons[0]

    def damage_current_weapon(self):
        if self.current_weapon()._damage():
            self.weapons.remove(0)

class Weapon:
    def __init__(self, name, damage, durability):
        self.name=name
        self.damage=damage
        self.durability=durability

    def _damage(self):
        self.durability--
        return True if self.durability==0 else False


class ArmorPiece:
    def __init(self, name, prot):
        self.prot=prot
