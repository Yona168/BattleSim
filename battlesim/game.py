from random import sample
from enum import Enum, auto
class Turn:
    def __init__(self, entity_one, entity_two):
        self.entity_one=entity_one
        self.entity_two=entity_two

    def resolve(self):
        def _resolve_speed():
            first=self.entity_one
            second=self.entity_two
            if self.entity_one.speed==self.entity_two.speed:
                first=sample([self.entity_one, self.entity_two],1)
                second=self.entity_one if first==self.entity_two else self.entity_one
            else:
                sorted_list=sorted([self.entity_one, self.entity_two], key=lambda entity: entity.speed)
                first=sorted_list[0]
                second=sorted_list[1]
            return (first, second)

        (faster, slower)=_resolve_speed()
        faster_dmg=faster.damage(slower)
        slower_dmg=0
        if not slower.is_dead():
            slower_dmg=slower.damage(faster)
        self.faster_entity=faster
        self.slower_entity=slower
        self.faster_dmg=faster_dmg
        self.slower_dmg=slower_dmg
class State(Enum):
    ACTIVE=auto(),
    ENDED=auto();
class Game:
    def __init__(self,entity_one, entity_two, output_func):
        self.entity_one=entity_one
        self.entity_two=entity_two
        self.output_func=output_func
        self.turns=list()
        self.state=State.ACTIVE

    def progress(self):
        turn=Turn(self.entity_one, self.entity_two)
        turn.resolve()
        self.output_func(">>{0} hit {1} for {2} health!".format(turn.faster_entity.name, turn.slower_entity.name, turn.faster_dmg))
        if turn.slower_entity.is_dead():
            self.output_func(">>{0} died!".format(turn.slower_entity))
        else:
            self.output_func(">>{0} hit {1} for {2} health!".format(turn.slower_entity.name, turn.faster_entity.name, turn.slower_dmg))
            self.end()
        self.turns.append(turn)

    def end(self):
        self.output_func("Game has ended!")
        self.state=State.ENDED

    def is_active(self):
        return self.state==State.ACTIVE
