Ticket #8: The Armory (Composition)

Description: Right now, damage is intrinsic to the character. If the Hero finds a shiny sword, they can't use it. We need to create a Weapon system so characters can equip items to boost their damage.

Requirements:

    Create a Weapon class (models.py):

        It needs an __init__ with:

            name (String, e.g., "Iron Sword")

            damage (Integer, e.g., 5)

        Add a __str__ method so it prints nicely (e.g., <Iron Sword (5 DMG)>).

    Update Character class (models.py):

        New Attribute: In __init__, add self.weapon = None. (Everyone starts unarmed).

        New Method: Add equip(self, weapon).

            This takes a Weapon object and saves it to self.weapon.

            Print: "[Name] equipped [Weapon Name]!"

        Update attack Method:

            Calculated the total damage.

            Logic: Base Strength + Weapon Damage (if they have one).

            Note: You'll need an if self.weapon: check. If they are unarmed, damage is just strength.

    Update main.py:

        Create an instance of Weapon (e.g., "Excalibur" with 20 damage).

        Before the loop starts, have the character_one (Hero) equip the weapon.

        Run the battle. The Hero should now be hitting much harder.

Acceptance Criteria:

    The Hero attacks for (Strength + Weapon Damage).

    The Goblin (who has no weapon) still attacks for just Strength.

    You clearly see the "Equipped" message in the log.

Concept:

    This is Object Composition. You are passing a Weapon object into a Character object. The Character "owns" the Weapon.