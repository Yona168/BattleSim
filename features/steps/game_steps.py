from behave import *
import battlesim
import copy


@given("Both entities have 1000 HP, are of the same type and have a weapon that does 3 damage")
def setup_entities(context):
    def generate_entity():
        weapon=Weapon("Weak Sword",3,1000)
        inv=Inventory(weapons=list(weapon))
        return Entity("Weakling",1000,inv,5)
    context.entity_one=generate_entity()
    context.entity_two=generate_entity()
    context.entity_one_health=copy.deepcopy(context.entity_one.health)
    context.entity_two_health=copy.deepcopy(context.entity_two.health)

@when("They attack each other for {amount} turns")
def attacking(context):
    game=Game(context.entity_one, context.entity_two, print)
    for i in (0,amount):
        game.progress()

@then("They should both have {relation} health")
def check_health_lost(context):
    (one_old, one_new)=(context.entity_one_health, context.entity_one.health)
    (two_old, two_new)=(context.entity_two_health, context.entity_two.health)
    if relation=="less":
        assert(one_new<one_old and two_new<two_old)
    elif relation=="more":
        assert(one_new>one_old and two_new>two_old)
    elif relation=="the same":
        assert(one_new==one_old and two_new==two_old and two_new==one_new)
    else:
        context.self.fail('Invalid argument {context}')
