from inventory import Inventory
from element import EntityType
from random import uniform
class Entity:
    def __init__(self, health, inventory, speed, type=EntityType.NEUTRAL):
        self.health=health
        self.inventory=inventory
        self.speed=speed
        self.type=type

    def _armor_protection(self):
        return sum(map(lambda armor: armor.prot, self.inventory.armor))

    def _total_damage(self):
        return self.inventory.current_weapon().damage

    def damage(self, other_entity):
        __basic_dmg=((self._total_damage()-other_entity._armor_protection()))*self.type.multiplier(other_entity.type)
        dmg_amt=abs(round(uniform(__basic_dmg-3, __basic_dmg+3), 2))
        __weapon=self.inventory.current_weapon().damage

        other_entity.health-=dmg_amt
        return dmg_amt
