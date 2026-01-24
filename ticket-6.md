Ticket #6: Encapsulation (Protecting the Data)

Description: Right now, our objects are very "promiscuous." Any code can reach inside a character and change their health directly (target.hp -= ...). This is risky. What if we accidentally set HP to -50? Or what if we want to trigger a sound effect every time damage is taken? We need to Encapsulate the logic for taking damage.

Requirements:

    Update Character class (models.py):

        Rename self.hp to self._hp (add the underscore).

            Note: In Python, a leading underscore signals to other developers: "This is private! Don't touch it directly."

        Update your __str__ and is_alive methods to use self._hp.

        Create a new method: take_damage(self, damage_amount).

            Logic:

                Subtract damage_amount from self._hp.

                Validation: If self._hp drops below 0, set it to 0. (No negative HP allowed).

                Optional: You can print a debug message here like " [Name] took [amount] dmg. Remaining HP: [hp]".

        Update attack method:

            Instead of target.hp -= self.strength, allow the target to handle it:

            target.take_damage(self.strength)

    Update Warrior and Mage (models.py):

        Update Mage.attack to use target.take_damage(self.intelligence).

        Update Warrior.heal to modify self._hp.

    Update main.py:

        Any reference to .hp needs to be fixed.

        If you are checking character_one.hp < 30, we have a problem: _hp is private.

        Fix: Add a "Getter" method to Character called get_hp(self) that simply returns self._hp. Use that in your main loop comparison.

Acceptance Criteria:

    _hp is never accessed directly in main.py (only via methods).

    HP never displays as a negative number (stops at 0).

    The battle flow remains the same.

Hint:

    You are shifting the responsibility. The Attacker shouldn't calculate the victim's health. The Attacker should just deliver the damage, and the Victim calculates the result.