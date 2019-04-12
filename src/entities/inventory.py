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

class Weapon:
    def __init__(self, name, damage):
        this.name=name
        this.damage=damage
    
class ArmorPiece:
    def __init(self, name, prot):
        this.prot=prot
