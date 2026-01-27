Ticket #7 with this understanding

Now, let's implement the logic. We are intercepting the assignment to validate the data.

Requirements for models.py (Character class):

    Storage (__init__):

        We need a place to actually store the data that isn't the property name.

        Store self._hp = hp (The private storage).

        Store self._max_hp = hp (To compare against later).

    The Interceptor (The Getter):

        Create a method def hp(self):.

        Decorate it with @property.

        It should return self._hp.

    The Validator (The Setter):

        Create a method def hp(self, value):.

        Decorate it with @hp.setter.

        The Logic:

            Check if value > self._max_hp. If yes, assign self._max_hp to self._hp.

            Check if value < 0. If yes, assign 0 to self._hp.

            Else, assign value to self._hp.

    Usage (Refactor):

        Update take_damage: Change logic to self.hp -= damage.

            Why? This triggers the Setter. The Setter handles the < 0 check.

        Update Warrior.heal: Change logic to self.hp += 10.

            Why? This triggers the Setter. The Setter handles the > max_hp check.

Give this a try. You are writing the logic that sits between the assignment and the storage.