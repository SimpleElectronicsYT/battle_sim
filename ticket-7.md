Ticket #7: Pythonic Encapsulation (Properties)

Description: We have protected _hp from being set to a negative number via take_damage. However, Warrior.heal modifies self._hp directly (self._hp += 10).

    If the Warrior heals, they could technically exceed their starting HP (e.g., go from 100 to 110). We don't want that.

    If we write self.hp -= 5 anywhere else, it would crash or bypass our checks.

In Python, we don't usually write get_hp() and set_hp(). We use Decorators to make a method act like a variable. This allows us to add logic (like "don't go above Max HP") every time the variable changes.

Requirements:

    Update Character class (models.py):

        Max HP: In __init__, store the starting HP in a new variable: self._max_hp.

        The Getter: Create a method named hp(self) and put the @property decorator above it. It should just return self._hp.

        The Setter: Create a method named hp(self, value) and put the @hp.setter decorator above it.

            Logic:

                Update self._hp to the new value.

                Clamp it: If self._hp > self._max_hp, set it back to _max_hp.

                Clamp it: If self._hp < 0, set it to 0.

    Refactor Methods (models.py):

        take_damage: You can delete the "if < 0" logic inside this method. Now, you can simply write self.hp -= damage_amount. The setter will automatically catch the negative number and fix it!

        Warrior.heal: Change self._hp += 10 to self.hp += 10. The setter will automatically prevent it from going over 100!

    Refactor main.py:

        Check your print statements or logic. You can now safe usage character.hp (without the underscore) because the @property exposes it nicely.

Acceptance Criteria:

    The Warrior cannot heal above their starting HP (e.g., if they are at 95/100 and heal for 10, they stop at 100).

    The logic for "clamping" HP is centralized in one place (the setter), not scattered across heal and take_damage.

Hint:

    The syntax looks like this:
    Python

    @property
    def hp(self):
        return self._hp

    @hp.setter def hp(self, value): self._hp = value # add checks here