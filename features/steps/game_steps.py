from behave import *
from battlesim import Weapon, Game, Inventory, Entity, EntityType
import copy
from hamcrest import assert_that, equal_to
import logging


@given("Both entities have 1000 HP, are of the same type and have a weapon that does 3 damage")
def setup_entities(context):
    def generate_entity():
        weapon=Weapon("Weak Sword",3,1000)
        inv=Inventory(weapons=[weapon])
        return Entity("Weakling",1000,inv,5)
    context.entity_one=generate_entity()
    context.entity_two=generate_entity()
    context.entity_one_health=copy.deepcopy(context.entity_one.health)
    context.entity_two_health=copy.deepcopy(context.entity_two.health)

@given('Two entities, faster is of type "{type_one}" and slower is of type "{type_two}"')
def setup_type_game(context, type_one, type_two):
    context.entity_one=Entity("Faster Entity",10000, Inventory(), 10, type=EntityType[type_one])
    context.entity_two=Entity("Slower Entity",10000, Inventory(), 5, type=EntityType[type_two])
@given("They both have no armor")
def ensure_no_armor(context):
    context.entity_one.inventory.armor.clear()
    context.entity_two.inventory.armor.clear()

@given("Both entity's weapons do 5 damage and bypass offsets")
def give_weapons(context):
    def get_weapon():
        weapon=Weapon("Weak Gun",5,10000)
        weapon._bypass_offset=True
        return weapon
    context.entity_one.inventory.weapons.append(get_weapon())
    context.entity_two.inventory.weapons.append(get_weapon())

@given("One entity is buffed out, the other is a 1 health weakling")
def setup_unfair_match(context):
    op_sword=Weapon("Death Bringer",999,1000)
    context.entity_one=Entity("Bully", 10000, Inventory(weapons=[op_sword]), 100)
    weak_mace=Weapon("Weak Mace",1,1)
    context.entity_two=Entity("Subject",1, Inventory(weapons=[weak_mace]),1)

@when('They attack each other for "{amount}" turns')
def attacking(context, amount):
    game=Game(context.entity_one, context.entity_two, logging.info)
    for i in range(0,int(amount)):
        game.progress()
    context.game=game

@then("The weakling should be dead")
def weakling_dead(context):
    assert(context.entity_two.is_dead())

@then("The game should be over")
def game_over(context):
    assert(not context.game.is_active())

@then('they should both have "{relation}" health')
def check_health_lost(context, relation):
    (one_old, one_new)=(context.entity_one_health, context.entity_one.health)
    (two_old, two_new)=(context.entity_two_health, context.entity_two.health)
    if relation=="less":
        assert(one_new<one_old and two_new<two_old)
    elif relation=="more":
        assert(one_new>one_old and two_new>two_old)
    elif relation=="the same":
        assert(one_new==one_old and two_new==two_old and two_new==one_new)
    else:
        fail('Invalid argument {0}'.format(relation))

@then('The faster one should have dealt "{damage}" damage')
def check_damage(context, damage):
    assert(context.game.turns[0].faster_dmg==float(damage))
