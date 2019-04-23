from random import uniform
from .element import EntityType
class Entity:
    def __init__(self, name, health, inventory, speed, type=EntityType.NEUTRAL):
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
        __offset=__basic_dmg*(.2*__basic_dmg)
        dmg_amt=round(min(uniform(__basic_dmg-__offset, __basic_dmg+__offset), 0), 2)
        other_entity.health-=dmg_amt
        self.inventory.damage_current_weapon()
        return dmg_amt

    def is_dead(self):
        return self.health==0
