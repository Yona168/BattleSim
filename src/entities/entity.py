from inventory import Inventory
from element import EntityType
class Entity:
    def __init__(self, health, inventory, type=EntityType.NEUTRAL):
        self.health=health
        self.inventory=inventory
        self.type=type

    def _armor_protection(self):
        return sum(map(lambda armor: armor.prot, self.inventory.armor))

    def _total_damage(self):
        return sum(map(lambda weapon: weapon.damage, self.inventory.weapons))

    def damage(self, other_entity):
        dmg_amt=((self._total_damage()-other_entity._armor_protection()))*self.type.multiplier(other_entity.type)
        other_entity.health-=dmg_amt
        return dmg_amt
