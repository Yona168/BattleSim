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
