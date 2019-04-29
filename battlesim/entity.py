from random import uniform
from .element import EntityType
from copy import deepcopy
class Entity:
    def __init__(self, name, health, inventory, speed, type=EntityType.NEUTRAL):
        self.health=health
        self.inventory=inventory
        self.speed=speed
        self.type=type
        self.name=name

    def _armor_protection(self):
        return sum(map(lambda armor: armor.prot, self.inventory.armor))

    def _total_damage(self):
        return self.inventory.current_weapon().damage

    def damage(self, other_entity):
        __basic_dmg=((self._total_damage()-other_entity._armor_protection()))*self.type.multiplier(other_entity.type)
        end_dmg=0
        if not self.inventory.current_weapon()._bypass_offset:
            __offset=__basic_dmg*.2
            end_dmg=round(uniform(__basic_dmg-__offset, __basic_dmg+__offset),2)
        end_dmg=0 if end_dmg<0 else __basic_dmg
        other_entity.health-=end_dmg
        other_entity.health=0 if other_entity.health<0 else other_entity.health
        self.inventory.damage_current_weapon()
        return end_dmg

    def is_dead(self):
        return self.health==0

    def snapshot(self):
        return Entity(deepcopy(self.name), deepcopy(self.health), deepcopy(self.speed), deepcopy(self.inventory), type)
