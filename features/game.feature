Feature: Entities damaging each other

Scenario: Random Damaging
  Given Both entities have 1000 HP, are of the same type and have a weapon that does 3 damage
  When They attack each other for "5" turns
  Then they should both have "less" health

Scenario: No Damage
  Given Both entities have 1000 HP, are of the same type and have a weapon that does 3 damage
  When They attack each other for "0" turns
  Then they should both have "the same" health

Scenario: Death
  Given One entity is buffed out, the other is a 1 health weakling
  When They attack each other for "1" turns
  Then The game should be over
  And the weakling should be dead

Scenario Outline: Type Advantages
  Given Two entities, faster is of type "<type_one>" and slower is of type "<type_two>"
  And they both have no armor
  And both entity's weapons do 5 damage and bypass offsets
  When They attack each other for "1" turns
  Then the faster one should have dealt "<damage>" damage

  Examples: Advantages
    |type_one  |type_two     | damage |
    |FIRE      |GRASS        | 10     |
    |WATER     |FIRE         | 10     |
    |GRASS     |WATER        | 10     |

  Examples: Disadvantages
    |type_one  |type_two     | damage |
    |GRASS     |FIRE         | 2.5    |
    |FIRE      |WATER        | 2.5    |
    |WATER     |GRASS        | 2.5    |

  Examples: Neutral
    |type_one  |type_two     | damage |
    |GRASS     |NEUTRAL      | 5      |
    |FIRE      |NEUTRAL      | 5      |
    |WATER     |NEUTRAL      | 5      |
    |GRASS     |GRASS        | 5      |
    |NEUTRAL   |FIRE         | 5      |
    |NEUTRAL   |WATER        | 5      |
    |NEUTRAL   |NEUTRAL      | 5      |
