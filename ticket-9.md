Ticket #9: Lists & The Inventory

Description: One weapon is boring. Characters in RPGs are pack mules. They carry potions, keys, and backup swords. We need a way to store multiple items. This is where Lists come in.

Requirements:

    Update Character (models.py):

        In __init__, add a new attribute: self.inventory = []. (An empty list).

        Create a method pick_up(self, item).

            Logic: Append the item to self.inventory.

            Print: "[Name] picked up [Item Name]!"

        Create a method show_inventory(self).

            Logic: Loop through self.inventory.

            Print: Print the str() of every item in the list.

            Hint: print("Inventory:", [str(item) for item in self.inventory]) is a fancy way, or just a for loop works too.

    Update main.py:

        Create a Weapon("Dagger", 5).

        Create a Weapon("Greatsword", 30).

        Have the Hero pick_up both.

        Call character_one.show_inventory() before the fight starts.

        Note: You don't need to equip them yet, just prove you can carry them.

Acceptance Criteria:

    The code prints a list showing both the Dagger and the Greatsword in the Hero's possession.

    The Battle still runs normally (with Excalibur equipped).

This is a low-stress ticket. Just standard Python lists.