Ticket #4: Inheritance (The Warrior Class)

Description: We want to distinguish our Hero from the common rabble. We need a specialized class for the player.

Requirements:

    Update models.py:

        Create a new class called Warrior that inherits from Character.

        Do not write a new __init__ method for the Warrior (it will automatically use the one from Character).

        Add a new method unique to the Warrior called heal.

            Logic: It should add 10 to the Warrior's hp.

            Print: "Warrior casts Heal! HP is now [new_hp]."

    Update main.py:

        Change character_one so it is an instance of Warrior (instead of Character).

        Inside your battle loop, add a logic check for the Hero's turn:

            If the Hero's HP is less than 30, call heal() instead of attack().

            Else, attack as normal.

Acceptance Criteria:

    The code runs without errors.

    When the Hero gets low on health (below 30), they stop attacking and heal themselves.

    The Goblin continues to attack the Hero during the healing turns.

Hint:

    To make one class inherit from another, use parentheses in the definition: class ChildClass(ParentClass):