from random import sample
from entity import Entity
class Turn:
    def __init__(self, entity_one, entity_two):
        self.entity_one=entity_one
        self.entity_two=entity_two

    def resolve():
        def _resolve_speed():
            first=self.entity_one
            second=self.entity_two
            if self.entity_one.speed==self.entity_two.speed:
                first=sample([self.entity_one, self.entity_two],1)
                second=self.entity_one if first==self.entity_two else entity_one
            else:
                sorted_list=sorted([self.entity_one, self.entity_two], key=lambda entity: entity.speed)
                first=sorted_list[0]
                second=sorted_list[1]
            return (first, second)

        (faster, slower)=_resolve_speed()
