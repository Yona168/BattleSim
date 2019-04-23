class Inventory:
    def __init__(self, armor=list(), weapons=list(), other_items=list()):
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
        if len(self.weapons)==0:
            self.weapons.append(__default_weapon())
        return self.weapons[0]

    def damage_current_weapon(self):
        if self.current_weapon()._damage():
            self.weapons=[__default_weapon()] if len(self.weapons)==0 else self.weapons[1:]

    def __default_weapon():
        return Weapon("Fists",1,10)

class Weapon:
    def __init__(self, name, damage, durability):
        self.name=name
        self.damage=damage
        self.durability=durability

    def _damage(self):
        self.durability-=1
        return True if self.durability==0 else False


class ArmorPiece:
    def __init(self, name, prot):
        self.prot=prot
