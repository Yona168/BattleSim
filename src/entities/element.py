from enum import Enum

class Type:
    def __init__(self):
        self.strength=0
        self.weakness=0

class EntityType(Enum):
    FIRE=Type()
    GRASS=Type()
    WATER=Type()
    NEUTRAL=Type()
    FIRE.strength=GRASS
    FIRE.weakness=WATER
    GRASS.strength=WATER
    GRASS.weakness=FIRE
    WATER.strength=FIRE
    WATER.weakness=GRASS

    def multiplier(self,type):
        if self.weakness==type:
            return .5
        elif self.strength==type:
            return 2
        else:
            return 1
    
