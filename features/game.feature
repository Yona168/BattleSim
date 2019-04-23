Feature: Entities damaging each other

Scenario: Random Damaging
Given: Both entities have 1000 HP, are of the same type and have a weapon that does 3 damage
When: They attack each other for 5 turns
Then: They should both have less health

Scenario: No Damage
Given: Both entities have 1000 HP, are of the same type and have a weapon that does 3 damage
When: They attack each other for 0 turns
Then: They should both have the same health
